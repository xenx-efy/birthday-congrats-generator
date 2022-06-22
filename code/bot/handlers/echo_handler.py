from telegram import Update
from telegram.ext import CallbackContext

from .handler import Handler


class EchoHandler(Handler):

    def handle(self, update: Update, context: CallbackContext):
        update.message.reply_text(update.message.text)
