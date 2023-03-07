class TakeView:
  def __init__(self, toy_titles):
    self.toy_titles = toy_titles


  def render(self):
    print(f'Поздравляю!')
    print(f'Вы получили следующие игрушки: {", ".join(self.toy_titles)}!')
    print('')
