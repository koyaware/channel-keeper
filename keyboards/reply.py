from aiogram.types import ReplyKeyboardMarkup

from buttons.reply import ADD_CHANNEL, VIEW_CHANNELS, DELETE_CHANNEL

USER_KEYBOARDS = ReplyKeyboardMarkup([
    [ADD_CHANNEL, VIEW_CHANNELS],
    [DELETE_CHANNEL]
], resize_keyboard=True)