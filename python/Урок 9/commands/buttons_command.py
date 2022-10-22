from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from game import Game

async def buttons_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  query = update.callback_query

  await query.answer()

  if query.data != 'repeat':
    game = Game(query.data)
  else:
    game = Game()

  reply_markup = InlineKeyboardMarkup(game.buttons())
  await query.edit_message_text(text=game.text(), reply_markup=reply_markup)
