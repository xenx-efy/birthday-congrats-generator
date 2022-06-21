from telegram.ext import Updater

# from handler_router import HandlerRouter
from .handler_router import HandlerRouter


def start():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5413064554:AAG0ATotIPk06T9M9_DtG8v3DL462Vx0rD4")

    HandlerRouter.route(updater.dispatcher)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
