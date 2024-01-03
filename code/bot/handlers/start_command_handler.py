from telegram import Update, ForceReply
from telegram.ext import CallbackContext

from .handler import Handler


class StartCommandHandler(Handler):
    """
    Handles '/start' command
    """

    async def handle(self, update: Update, context: CallbackContext):
        """Send a message when the command /start is issued."""
        user = update.effective_user
        await update.message.reply_markdown_v2(
            fr'Hi {user.mention_markdown_v2()}\!'
        )
