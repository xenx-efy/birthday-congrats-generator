from telegram import Update
from telegram.ext import CallbackContext

from ...congrats_generator.builder.birthday_congrats_builder import \
    BirthdayCongratsBuilder
from ...congrats_generator.director.congrats_builder_director import \
    CongratsBuilderDirector
from ...congrats_generator.model.congratulation import Congratulation
from .handler import Handler


class BirthdayCongratsHandler(Handler):
    def handle(self, update: Update, context: CallbackContext):
        builder = BirthdayCongratsBuilder()
        director = CongratsBuilderDirector()
        director.builder = builder

        director.build_long_congrats()

        congratulation: Congratulation | None = builder.congratulation
        if congratulation is not None:
            update.message.reply_text(congratulation.list_parts())
