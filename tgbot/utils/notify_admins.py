import logging

from aiogram import Dispatcher

from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    print("Бот Запущен")
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот Запущен", disable_notification=True)
        except Exception as err:
            logging.exception(err)
