from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from aiogram import Dispatcher, Bot
from asyncio import run
from aiogram.filters import CommandStart
from aiogram.types import Message
from .routers.register import register_router
from loguru import logger

dp = Dispatcher()
bot = Bot(token="6230284749:AAFAeqz29Afj6PA2TXinqmj2wHZD09JfFLk")

i18n = I18n(path="tele_trans/locales", default_locale="en", domain="messages")
dp.message.middleware(SimpleI18nMiddleware(i18n))


@dp.message(CommandStart())
async def message_handler(message: Message, i18n: I18n):
    _ = i18n.gettext
    await message.answer(_("Banner"))


dp.include_router(register_router)


@dp.startup()
async def on_start():
    bot_user = await bot.me()
    logger.info(f"bot started. botname: {bot_user.username}")


async def main():
    logger.info("starting ...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
