import os

from telegram.ext import ApplicationBuilder, CommandHandler

from .handlers.birthday_congrats_handler import BirthdayCongratsHandler
from .handlers.shot_handler import ShotCongratsHandler
from .handlers.start_command_handler import StartCommandHandler


def start():
    """Start the bot."""

    telegram_token = os.getenv('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(telegram_token).build()

    handlers = [CommandHandler('start', StartCommandHandler().handle),
                CommandHandler('birthday', BirthdayCongratsHandler().handle),
                CommandHandler('shot', ShotCongratsHandler().handle)]

    application.add_handlers(handlers)

    application.run_polling()
