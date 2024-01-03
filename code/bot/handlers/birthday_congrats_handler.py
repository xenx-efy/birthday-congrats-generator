from telegram import Update
from telegram.ext import CallbackContext

from .handler import Handler
from ...congrats_generator.builder.birthday_congrats_builder import BirthdayCongratsBuilder
from ...congrats_generator.director.congrats_builder_director import CongratsBuilderDirector


class BirthdayCongratsHandler(Handler):

    async def handle(self, update: Update, context: CallbackContext):
        builder = BirthdayCongratsBuilder()
        director = CongratsBuilderDirector()
        director.builder = builder

        director.build_long_congrats()

        congratulation = builder.congratulation.list_parts()

        await update.message.reply_text(congratulation)
