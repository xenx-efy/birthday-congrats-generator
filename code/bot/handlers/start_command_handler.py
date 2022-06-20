from telegram import Update, ForceReply
from telegram.ext import CallbackContext

import handler


class StartCommandHandler(handler.Handler):

    def handle(self, update: Update, context: CallbackContext):
        """Send a message when the command /start is issued."""
        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'Hi {user.mention_markdown_v2()}\!',
            reply_markup=ForceReply(selective=True),
        )
