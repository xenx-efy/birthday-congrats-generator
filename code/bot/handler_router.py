import telegram.ext
from telegram.ext import CommandHandler, MessageHandler, Filters

from .handlers.echo_handler import EchoHandler
from .handlers.start_command_handler import StartCommandHandler


class HandlerRouter:
    @staticmethod
    def route(dispatcher: telegram.ext.dispatcher.Dispatcher):
        # Start command handler
        dispatcher.add_handler(CommandHandler("start", StartCommandHandler().handle))

        # Echo handler
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, EchoHandler().handle))
