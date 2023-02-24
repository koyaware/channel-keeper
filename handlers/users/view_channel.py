from aiogram import Dispatcher
from aiogram.types import Message

from commands.user_commands import Commands
from models.models import Channels


async def view_channels(message: Message):
    channels: Channels = await Channels.query.where(
        Channels.user_id == message.from_user.id).gino.all()
    if not channels:
        await message.answer("У вас нет отслеживаемых каналов!")
    for channel in channels:
        await message.bot.send_message(message.from_user.id, f"Название: <b>{channel.name}</b>\n"
                                                             f"Канал: <b>{channel.link}</b>",
                                       disable_web_page_preview=True)


def register_view_channels_handler(dp: Dispatcher):
    dp.register_message_handler(
        view_channels, text=[Commands.view_channels.value])
