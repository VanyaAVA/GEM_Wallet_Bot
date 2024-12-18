from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Ваш API токен
API_TOKEN = "7893660360:AAEuwPJXlvosDya3U_K_dXpBxylvnyPIX4I"

# Функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Добро пожаловать в GEM Wallet! 💎\nКошелек находится в разработке.")

# Основная функция для запуска бота
def main():
    print("Инициализация...")

    # Создаем приложение (аналог Updater в старой версии)
    application = Application.builder().token(API_TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
