from telegram import Update
from telegram.ext import CallbackContext

from .handler import Handler
from ...congrats_generator.builder.shot_builder import ShotCongratsBuilder
from ...congrats_generator.director.congrats_builder_director import CongratsBuilderDirector


class ShotCongratsHandler(Handler):

    def handle(self, update: Update, context: CallbackContext):
        builder = ShotCongratsBuilder()

        director = CongratsBuilderDirector()
        director.builder = builder

        director.build_shot_congrats()

        congratulation = builder.congratulation.list_parts()

        update.message.reply_text(congratulation)
