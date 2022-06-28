import code.bot.main
import logging

import dotenv

dotenv.load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logger = logging.getLogger(__name__)


def main() -> None:
    code.bot.main.start()


if __name__ == "__main__":
    main()
