from model import Model

class ShowAction:
  def __init__(self):
    pass

  def call(self):
    print('Карточка заметки')
    print('')

    notes = Model.all()

    index = int(input('Укажите номер заметки: ')) - 1
    note = notes[index]

    print('')
    print(f'Заголовок: {note.title}')
    print(f'Описание:  {note.body}')
    print(f'Время:     {note.pretty_timestamp()}')
    print('')
