# Congrats Generator
Генерирует поздравления с днём рождения.

## Требования
- [Poetry](https://python-poetry.org/)

## Установка
1. Скопировать `.env.example` файл и переименовать в `.env`;
2. Заполнить параметр `TELEGRAM_TOKEN`. Получить его можно в [BotFather](https://telegram.me/BotFather);
3. Запустить установку зависимостей `poetry install`.

### Deploy
[How to host bot](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Hosting-your-bot)

Create a new screen and attach to it:

```shell
screen -S mybot
```

Start the bot:

```shell
python3 bot.py
```