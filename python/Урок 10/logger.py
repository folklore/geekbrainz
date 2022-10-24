from telegram import Bot
from telegram.constants import ParseMode

class Logger():
  TOKEN = 'TOKEN'
  LOG_CHAT_ID = -1001837640893


  def __init__(self):
    self.bot = Bot(self.TOKEN)


  async def send(self, user_id, text):
    message = f'User {user_id}\n<pre>{text}</pre>'

    await self.bot.send_message(
      chat_id=self.LOG_CHAT_ID,
      text=message,
      parse_mode=ParseMode.HTML
    )
