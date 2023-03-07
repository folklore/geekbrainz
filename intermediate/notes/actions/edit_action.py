from model import Model

class EditAction:
  def __init__(self):
    pass

  def call(self):
    print('Редактирование заметки')
    print('')

    notes = Model.all()

    index = int(input('Укажите номер заметки: ')) - 1
    note = notes[index]

    title = input(f'Укажите заголовок заметки [{note.title}]: ')
    body = input(f'Укажите описание заметки [{note.body}]: ')

    if title != '':
      note.title = title
    if body != '':
      note.body = body

    if title != '' or body != '':
      note.touch()

    Model.clean()

    for note in notes:
      note.save()

    print('')
    print('Заметка успешно обновлена')
    print('')
