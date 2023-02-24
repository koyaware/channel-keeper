from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from commands.user_commands import Commands
from misc.state import DeleteChannelState
from models.models import Channels


async def delete_channel(message: Message):
    channels = await Channels.query.where(
        Channels.user_id == message.from_user.id).gino.all()
    if not channels:
        await message.answer("У вас нет отслеживаемых каналов!")
    keyboard = InlineKeyboardMarkup()
    for channel in channels:
        keyboard.add(InlineKeyboardButton(
            channel.name,
            callback_data=channel.Id
        ))
    await DeleteChannelState.callback_query.set()
    await message.answer("Выберите канал который хотите удалить!", reply_markup=keyboard)


async def delete_channel_callback(callback: CallbackQuery, state: FSMContext):
    channel: Channels = await Channels.query.where(
        Channels.Id == int(callback.data)).gino.first()
    if not channel:
        await callback.bot.send_message(
            callback.from_user.id,
            "Произошла ошибка...")
    else:
        await channel.delete()
        await callback.bot.send_message(
            callback.from_user.id,
            "Успешно удалил!"
        )
        await callback.bot.delete_message(
            callback.from_user.id,
            callback.message.message_id)
    await state.finish()


def register_delete_channel_handlers(dp: Dispatcher):
    dp.register_message_handler(
        delete_channel, text=[Commands.delete_channel.value])
    dp.register_callback_query_handler(
        delete_channel_callback, state=DeleteChannelState.callback_query)