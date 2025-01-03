
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Application

from app.config import Config
from app.di import init_container
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Нажми меня", callback_data='button_pressed')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Нажми кнопку ниже:', reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Кнопка была нажата!")

def main() -> None:
    container = init_container()
    config = container.resolve(Config)
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(config.TELEGRAM_KEY).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()