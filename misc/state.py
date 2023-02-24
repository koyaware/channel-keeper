from aiogram.dispatcher.filters.state import StatesGroup, State


class FollowChannelState(StatesGroup):
    channel_link = State()
    channel_name = State()


class DeleteChannelState(StatesGroup):
    callback_query = State()