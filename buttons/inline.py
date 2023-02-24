from aiogram.types import InlineKeyboardButton

NEXT = InlineKeyboardButton("⏭️", callback_data="next")
PREV = InlineKeyboardButton("⏮️", callback_data="prev")
CANCEL = InlineKeyboardButton("❌", callback_data="cancel")