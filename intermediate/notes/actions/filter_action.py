from model import Model

class FilterAction:
  def __init__(self):
    pass

  def call(self):
    print('Список заметок по фильтру')
    print('')

    query = input('Укажите дату в формате ДД.ММ.ГГГГ или ключевое слово: ')
    print('')

    print(' ## |      Заголовок       |                Описание                |        Время')
    for index, note in enumerate(Model.all()):
      if query in note.to_row(index):
        print(note.to_row(index))
    print('')
