from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message = f'''Привет "{update.effective_user.first_name}"!
Я бот для генерации QR кодов.
Просто отправь мне текст, который нужно закодировать ...'''

  await update.message.reply_text(message)
