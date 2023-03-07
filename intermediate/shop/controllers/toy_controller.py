from storage import Storage
from models.toy import Toy

from views.toy.index_view import IndexView
from views.toy.new_view import NewView
from views.toy.edit_view import EditView
from views.toy.delete_view import DeleteView


class ToyController:
  def __init__(self):
    self.storage = Storage()


  def index(self):
    toys = self.storage.all()

    view = IndexView(toys)
    view.render()


  def new(self):
    view = NewView()
    view.render_greeting()

    attrs = [
      input('Введите название: '),
      input('Введите количество (>0): '),
      input('Введите частоту выпадания (>0 и <=100): '),
    ]

    id = len(self.storage.all()) + 1
    toy = Toy(id, *attrs)
    self.storage.save(toy)

    view.render(toy)


  def edit(self):
    view = EditView()
    view.render_greeting()

    toys = self.storage.all()

    index = int(input('Укажите номер игрушки: ')) - 1
    toy = toys[index]

    attrs = [
      input(f'Введите название [{toy.title}]: '),
      input(f'Введите количество (>0) [{toy.count}]: '),
      input(f'Введите частоту выпадания (>0 и <=100) [{toy.frequency}]: '),
    ]

    if attrs[0] != '':
      toy.title = attrs[0]
    if attrs[1] != '':
      toy.count = attrs[1]
    if attrs[2] != '':
      toy.frequency = attrs[2]

    self.storage.clean()

    for toy in toys:
      self.storage.save(toy)

    view.render(toy)


  def delete(self):
    view = DeleteView()
    view.render_greeting()

    toys = self.storage.all()

    index = int(input('Укажите номер игрушки: ')) - 1
    toy = toys[index]

    self.storage.clean()

    for current_index, toy in enumerate(toys):
      if current_index != index:
        self.storage.save(toy)

    view.render(toy)
