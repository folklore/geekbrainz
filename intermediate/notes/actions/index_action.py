from model import Model

class IndexAction:
  def __init__(self):
    pass

  def call(self):
    print('Список заметок')
    print('')

    print(' ## |      Заголовок       |                Описание                |        Время')
    for index, note in enumerate(Model.all()):
      print(note.to_row(index))
    print('')
