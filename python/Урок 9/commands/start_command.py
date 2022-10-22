from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from game import Game

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message = f'''Привет "{update.effective_user.first_name}"!
Я бот для игры в крестики-нолики.
Всё, игра началась ...'''
  await update.message.reply_text(message)

  game = Game()

  reply_markup = InlineKeyboardMarkup(game.buttons())
  await update.message.reply_text(text=game.text(), reply_markup=reply_markup)
