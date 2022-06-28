from telegram import Update
from telegram.ext import CallbackContext

from ...congrats_generator.builder.shot_builder import ShotCongratsBuilder
from ...congrats_generator.director.congrats_builder_director import \
    CongratsBuilderDirector
from .handler import Handler


class ShotCongratsHandler(Handler):
    def handle(self, update: Update, context: CallbackContext):
        builder = ShotCongratsBuilder()

        director = CongratsBuilderDirector()
        director.builder = builder

        director.build_shot_congrats()

        if builder.congratulation is not None:
            congratulation = builder.congratulation.list_parts()

            update.message.reply_text(congratulation)
