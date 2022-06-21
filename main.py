import logging
import code.bot.main

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# def keyboard():
#     return [
#         [
#             InlineKeyboardButton("1", callback_data=str(1)),
#             InlineKeyboardButton("2", callback_data=str(2)),
#         ]
#     ]


def main() -> None:
    code.bot.main.start()


if __name__ == '__main__':
    main()
