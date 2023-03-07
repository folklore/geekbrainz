class DeleteView:
  def __init__(self):
    pass


  def render_greeting(self):
    print('Удаление игрушки')
    print('')


  def render(self, toy):
    print(f'Игрушка "{toy.title}" успешно удалена.')
    print('')
