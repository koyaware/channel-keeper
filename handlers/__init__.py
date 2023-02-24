from aiogram import Dispatcher

from handlers.users import register_all_user_handlers


def register_all_handlers(dp: Dispatcher):
    register_all_user_handlers(dp)