from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message


class IsLink(BoundFilter):

    async def check(self, message: Message) -> bool:
        true_link = "https://t.me/"
        if true_link not in message.text.lower():
            await message.answer(f"Неправильная ссылка!\n"
                                  f"Пример ссылки: https://t.me/example",
                                  disable_web_page_preview=True)
            return False
        else:
            return True