from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
)
from telegram.ext import (
    Updater, CommandHandler, CallbackQueryHandler, CallbackContext
)
import os

# Получаем токен и URL из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://aligatorru.github.io/meowVSwoof/")

# Команда /start
def start(update: Update, context: CallbackContext):
    user = update.effective_user

    keyboard = [
        [InlineKeyboardButton("🎮 Запустить игру", web_app=WebAppInfo(url=WEBAPP_URL))],
        [InlineKeyboardButton("📜 Правила", callback_data="rules")],
        [InlineKeyboardButton("🧩 Режимы", callback_data="modes")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, {user.first_name}! 🐱🐶\nЭто бот для запуска игры Кошечки-собачки.\nВыбери действие ниже:",
        reply_markup=reply_markup
    )

# Обработка нажатий на кнопки
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "rules":
        keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data="back")]]
        query.edit_message_text(
            text="📜 *Правила игры:*\n"
                 "Это шуточная версия крестиков-ноликов 🧠\n"
                 "Выбираешь сторону — и смотришь, как всё закончится 🐾😉",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "modes":
        keyboard = [
            [InlineKeyboardButton("🐱 Кошечки-Собачки", web_app=WebAppInfo(url=f"{WEBAPP_URL}?mode=neutral"))],
            # [InlineKeyboardButton("👦 Мальчики-Девочки", web_app=WebAppInfo(url=f"{WEBAPP_URL}?mode=boy"))],
            # [InlineKeyboardButton("👧 Девочки-Мальчики", web_app=WebAppInfo(url=f"{WEBAPP_URL}?mode=girl"))],
            [InlineKeyboardButton("🔙 Назад", callback_data="back")]
        ]
        query.edit_message_text(
            text="🧩 Выберите версию игры:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "back":
        # Возвращаемся к главному меню
        user = query.from_user
        keyboard = [
            [InlineKeyboardButton("🎮 Запустить игру", web_app=WebAppInfo(url=WEBAPP_URL))],
            [InlineKeyboardButton("📜 Правила", callback_data="rules")],
            [InlineKeyboardButton("🧩 Режимы", callback_data="modes")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text=f"Привет, {user.first_name}! 🐱🐶\nЭто бот для запуска игры Кошечки-собачки.\nВыбери действие ниже:",
            reply_markup=reply_markup
        )

# Запуск бота
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
