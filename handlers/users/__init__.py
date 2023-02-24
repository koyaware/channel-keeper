from aiogram import Dispatcher

from .delete_channel import register_delete_channel_handlers
from .follow_channel import register_follow_channel_handlers
from .start import register_start_handler
from .view_channel import register_view_channels_handler


def register_all_user_handlers(dp: Dispatcher):
    register_delete_channel_handlers(dp)
    register_follow_channel_handlers(dp)
    register_view_channels_handler(dp)
    register_start_handler(dp)