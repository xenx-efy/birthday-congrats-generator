import logging
import dotenv
import code.bot.main

dotenv.load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    code.bot.main.start()
