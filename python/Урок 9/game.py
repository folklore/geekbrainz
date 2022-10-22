from games.field import Field
# TODO: Мб. вынести логику telegram из игры
from telegram import InlineKeyboardButton as TGIKB


class Game():
  def __init__(self, data='-|1,2,3,4,5,6,7,8,9|-'):
    number, cells, current_step = data.split('|')

    self.cells = cells.split(',')

    if number != '-' and current_step != '-':
      self.cells[int(number)] = current_step

    if current_step == '-' or current_step == '⭕️':
      self.next_step = '❌'
    else:
      self.next_step = '⭕️'

    self.winner = None


  def text(self):
    if self.to_be_continue():
      if self.next_step == '❌':
        text = '... ход крестиков ❌ ...'
      else:
        text = '... ход ноликов ⭕️ ...'
    else:
      if not self.drawn_game():
        text = f'... выиграли "{self.winner}"!'
      else:
        text = '... закончилось игровое поле, ничья!'
    return text


  def field(self):
    return Field(self.cells, self.next_step)


  def buttons(self):
    if self.to_be_continue():
      return self.field().build()
    else:
      return [[TGIKB('Повторить', callback_data='repeat')]]


  def to_be_continue(self):
    return not self.any_win() and not self.drawn_game()


  def any_win(self):
    # Проверка по горизонталям
    i = 0
    while i <= 2:
      if self.cells[i * 3 + 0] == self.cells[i * 3 + 1] and self.cells[i * 3 + 1] == self.cells[i * 3 + 2]:
        self.winner = self.cells[i * 3 + 0]
        break
      i += 1

    # Проверка по вертикалям
    j = 0
    while j <= 2:
      if self.cells[j + 0] == self.cells[j + 3] and self.cells[j + 3] == self.cells[j + 6]:
        self.winner = self.cells[j + 0]
        break
      j += 1

    # Диагональ вниз
    if self.cells[0] == self.cells[4] and self.cells[4] == self.cells[8]:
      self.winner = self.cells[0]

    # Диагональ вверх
    if self.cells[2] == self.cells[4] and self.cells[4] == self.cells[6]:
      self.winner = self.cells[2]

    return self.winner


  def drawn_game(self):
    return all([cell == '❌' or cell == '⭕️' for cell in self.cells])
