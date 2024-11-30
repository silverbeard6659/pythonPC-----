import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import openai

# Установите ваш API ключ OpenAI
openai.api_key = 'sk-72ff7213-a8d8-43d5-a4f6-e875d543cebe'

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я ваш ChatGPT бот. Пишите мне, и я отвечу!')

async def chat_with_gpt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    response = await chat_with_gpt(user_message)
    await update.message.reply_text(response)

def main() -> None:
    application = ApplicationBuilder().token('8070242198:AAEyXV4kkZe38mICpczCpa1_xNIP9HrPw7M').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
