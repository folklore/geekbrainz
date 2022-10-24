from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from commands.start_command import *
from commands.generate_command import *

app = ApplicationBuilder().token('TOKEN').build()

app.add_handler(CommandHandler('start', start_command))
app.add_handler(MessageHandler(~filters.COMMAND, generate_command))

print('Бот запущен. Для остановки нажмите "Ctrl+C"')
app.run_polling()
