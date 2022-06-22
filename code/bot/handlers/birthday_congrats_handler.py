from telegram import Update
from telegram.ext import CallbackContext

from .handler import Handler
from ...congrats_generator.congrats_generator import BirthdayCongratsBuilder, CongratsBuilderDirector


class BirthdayCongratsHandler(Handler):

    def handle(self, update: Update, context: CallbackContext):
        builder = BirthdayCongratsBuilder()
        director = CongratsBuilderDirector()
        director.builder = builder

        director.build_long_congrats()

        congratulation = builder.congratulation.list_parts()

        update.message.reply_text(congratulation)
