import os

from telegram.ext import Updater

# from handler_router import HandlerRouter
from .handler_router import HandlerRouter


def start():
    """Start the bot."""

    # Create the Updater and pass it your bot's token.
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(token=telegram_token if telegram_token else "")

    HandlerRouter.route(updater.dispatcher)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
