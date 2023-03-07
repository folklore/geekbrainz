from model import Model

class DeleteAction:
  def __init__(self):
    pass

  def call(self):
    print('Удаление заметки')
    print('')

    notes = Model.all()

    index = int(input('Укажите номер заметки: ')) - 1

    Model.clean()

    for current_index, note in enumerate(notes):
      if current_index != index:
        note.save()

    print('')
    print('Заметка успешно удалена')
    print('')
