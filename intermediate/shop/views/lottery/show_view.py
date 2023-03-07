class ShowView:
  def __init__(self, toy_titles):
    self.toy_titles = toy_titles


  def render(self):
    if(len(self.toy_titles) > 0):
      print(f'Игрушки подлежащие выдачи: {", ".join(self.toy_titles)}!')
    else:
      print(f'Игрушек подлежащих выдачи нет =(')
    print('')
