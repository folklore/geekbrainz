# TODO: Мб. вынести логику telegram из игры
from telegram import InlineKeyboardButton as TGIKB


class Field():
  def __init__(self, cells, next_step):
    self.cells = cells
    self.next_step = next_step


  def build(self):
    buttons = [TGIKB(c, callback_data=self.__data(i)) for i, c in enumerate(self.cells)]

    return [
      buttons[:3],  # 1 2 o
      buttons[3:6], # 4 x 6
      buttons[6:],  # x 8 o
    ]


  # Такой формат хранения данных
  #  позволит сделать игру асинхронной.
  #
  # Все данные для игры передаются с каждым шагом.
  #
  #   number (0-8)        step (x or o)
  #    |   9 cell values   |
  # => 6|x,x,o,x,o,-,-,-,-|o
  #
  def __data(self, number):
    cells = ','.join([cell for cell in self.cells])
    return f'{number}|{cells}|{self.next_step}'
