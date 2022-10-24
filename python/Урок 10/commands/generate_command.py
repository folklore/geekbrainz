from telegram import Update
from telegram.ext import ContextTypes

import io
import qrcode

from logger import Logger

logger = Logger()

async def generate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  file = qrcode.make(
    update.message.text,
    version=1,
    border=1
  )
  buf = io.BytesIO()

  file.save(buf, 'JPEG')
  buf.seek(0)

  await update.message.reply_photo(buf)
  await logger.send(update.effective_user.id, update.message.text)
