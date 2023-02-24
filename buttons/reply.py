from aiogram.types import KeyboardButton

from commands.user_commands import Commands

ADD_CHANNEL = KeyboardButton(Commands.add_channel.value)
VIEW_CHANNELS = KeyboardButton(Commands.view_channels.value)
DELETE_CHANNEL = KeyboardButton(Commands.delete_channel.value)