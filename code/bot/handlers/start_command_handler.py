from telegram import Update, User
from telegram.ext import CallbackContext

from .handler import Handler


class StartCommandHandler(Handler):
    """
    Handles '/start' command
    """

    def handle(self, update: Update, context: CallbackContext):
        """Send a message when the command /start is issued."""
        user: User | None = update.effective_user

        if user:
            update.message.reply_text(rf"Hi {user.mention_markdown_v2()}\!")
