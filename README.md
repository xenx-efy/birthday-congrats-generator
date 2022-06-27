# Birthday Congrats Generator

Generates birthday congrats example and put it into clipboard

## Requirements

- [Poetry](https://python-poetry.org/)

## Installation

Copy `.env.example` file as `.env` and put to it telegram token what you can receive
in [BotFather](https://telegram.me/BotFather).

Run `poetry install`.

## Deployment

> You can only run one bot per hash

### Locally

Just run `python main.py`

### Server
> I use heroku autodeploy on heroku's side, and don't responsible for efficiency

[Guide](https://github.com/python-telegram-bot/v13.x-wiki/wiki/Hosting-your-bot)

Create a new screen and attach to it:

```shell
screen -S mybot
```

Start the bot:

```shell
python3 bot.py
```

## Features

### Echo

Repeats every phrase what you send in chat.

## Commands

### `/birthday`

Generates birthday congratulation with introduction, body and ending.

### `/shot`

Generates short wish phrase like "хорошего настроения".