from aiogram import Dispatcher
from aiogram.types import Message

from commands.user_commands import Commands
from keyboards.reply import USER_KEYBOARDS
from models.models import Users


async def user_start(message: Message):
    user = await Users.query.where(
        Users.tg_id == message.from_user.id
    ).gino.first()
    if not user:
        await Users.create(
            tg_id=message.from_user.id)
    else:
        await message.answer(f"Здравствуйте, <b>{message.from_user.full_name}</b>!\n\n\n\n"
                             f"Вы можете нажать <b>{Commands.add_channel.value}</b>, чтобы добавить канал для отслеживания!"
                             f"\n\n\n"
                             f"Вы можете нажать <b>{Commands.view_channels.value}</b>, чтобы посмотреть отслеживаемые каналы!"
                             f"\n\n\n"
                             f"Вы можете нажать <b>{Commands.delete_channel.value}</b>, чтобы удалить отслеживаемый канал!"
                             , reply_markup=USER_KEYBOARDS)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(
        user_start, commands=['start'], state='*', commands_prefix='!/')