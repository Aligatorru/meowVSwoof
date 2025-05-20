from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 🔑 Вставь сюда токен твоего бота
TOKEN = 7963354488:AAFzhdfzjyBXSQJMHJl6howu0SAgHBu8iG4

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, {user.first_name}! Добро пожаловать в наше мини-приложение 🎉"
    )

    # ❗ Пытаемся удалить сообщение /start (сработает только в группах и если бот админ)
    try:
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
    except Exception as e:
        print(f"Не удалось удалить сообщение: {e}")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

if __name__ == '__main__':
    updater.start_polling()
    print("Бот запущен")
    updater.idle()
