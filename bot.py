from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.getenv("BOT_TOKEN")  # Безопасно получать токен из переменной окружения

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, {user.first_name}! Это бот от твоего мини-приложения 🎉"
    )

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    print("Бот запущен...")
    updater.start_polling()
    updater.idle()
