from model import Model

class NewAction:
  def __init__(self):
    pass

  def call(self):
    print('Добавление заметки')
    print('')

    title = input('Укажите заголовок заметки: ')
    body = input('Укажите описание заметки: ')

    note = Model(title, body)
    note.save()

    print('')
    print('Заметка успешно добавлена')
    print('')
