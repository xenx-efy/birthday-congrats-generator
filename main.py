import logging
from os import getenv

from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler

from dotenv import load_dotenv

from code.congrats_generator.congrats_generator import BirthdayCongratsBuilder, CongratsBuilderDirector

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def long_congrats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    builder = BirthdayCongratsBuilder()
    director = CongratsBuilderDirector()
    director.builder = builder

    director.build_long_congrats()

    congratulation = builder.congratulation.list_parts()

    await update.message.reply_text(text=congratulation)


if __name__ == '__main__':
    telegram_token = getenv('TELEGRAM_TOKEN')

    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    long_congrats_handler = CommandHandler('long', long_congrats)
    application.add_handler(long_congrats_handler)

    application.run_polling()
