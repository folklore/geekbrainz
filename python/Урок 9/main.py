from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from commands.start_command import *
from commands.buttons_command import *

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CallbackQueryHandler(buttons_command))

print('Бот запущен. Для остановки нажмите "Ctrl+C"')
app.run_polling()
