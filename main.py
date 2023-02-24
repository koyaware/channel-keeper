import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import load_config
from filters import register_all_filters
from handlers import register_all_handlers
from models.models import db


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Starting bot')
    config = load_config('.env')

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config
    register_all_handlers(dp)
    register_all_filters(dp)

    try:
        await db.set_bind(f'postgresql://'
                          f'{config.db.user}:{config.db.password}@'
                          f'{config.db.host}:5432/{config.db.database}')
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()
        await db.pop_bind().close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):

        logger.error('Bot stopped!')