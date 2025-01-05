from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
    Application,
    ContextTypes,
)

from app.application.telegram.mediator import ButtonMediator
from app.settings.config import Config
from app.di import init_container
from app.logic.services.handlers.check_price_handler import PriceCryptoHandler
from app.domain.mediators.base import BaseMediator


async def start(update: Update, context):
    # Создание кнопок
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data="button1")],
        [InlineKeyboardButton("Кнопка 2", callback_data="button2")],
    ]

    # Создание разметки с кнопками
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправка сообщения с кнопками
    await update.message.reply_text(
        "Привет! Выберите кнопку:", reply_markup=reply_markup
    )


# Функция обработки нажатия на кнопку
async def button(update: Update, context):
    query = update.callback_query
    data = query.data  # Получаем callback_data кнопки
    container = init_container()
    mediator: BaseMediator = container.resolve(ButtonMediator)
    await mediator.handle(data)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    container = init_container()
    result = container.resolve(PriceCryptoHandler)()
    await update.message.reply_text(update.message.text)


def main() -> None:
    container = init_container()
    config = container.resolve(Config)

    application = Application.builder().token(config.TELEGRAM_KEY).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
