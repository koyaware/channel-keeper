from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy import and_

from commands.user_commands import Commands
from filters import IsLink
from misc.state import FollowChannelState
from models.models import Channels


async def channels_name(message: Message):
    await message.answer("Пожалуйста, скиньте персональное наименование канала!\n"
                         "Пример: Мой первый отслеживаемый канал!")
    await FollowChannelState.channel_name.set()


async def pre_follow_channel(message: Message, state: FSMContext):
    name = await Channels.query.where(and_(
        Channels.name == message.text,
        Channels.user_id == message.from_user.id
    )).gino.all()
    if not name:
        await state.update_data(channel_name=message.text)
        await message.answer(f"Ваше персональное наименование канала: {message.text}")
        await message.answer("Пожалуйста, скиньте канал который нужно отслеживать!\n"
                             "Пример ссылки: https://t.me/example",
                             disable_web_page_preview=True)
        await FollowChannelState.channel_link.set()
    else:
        await message.answer("Выберите другое наименование канала!\n")


async def follow_channel(message: Message, state: FSMContext):
    async with state.proxy() as data:
        name_of_channel = data['channel_name']
    channel = await Channels.query.where(
        Channels.link == message.text).gino.all()
    if not channel:
        await Channels.create(
            link=message.text,
            user_id=message.from_user.id,
            name=name_of_channel
        )
        await state.update_data(channel_link=message.text)
        await message.answer("Успешно загрузил канал в базу данных для отслеживания!")
    else:
        await message.answer("Этот канал уже отслеживается!")
    await state.finish()


def register_follow_channel_handlers(dp: Dispatcher):
    dp.register_message_handler(
        channels_name, text=[Commands.add_channel.value])
    dp.register_message_handler(
        pre_follow_channel, state=FollowChannelState.channel_name)
    dp.register_message_handler(
        follow_channel, IsLink(), state=FollowChannelState.channel_link)