from models.item import Item

from views.items.index import ItemsView
from views.items.new import NewItemView
from views.items.edit import EditItemView
from views.items.delete import DeleteItemView

class ItemsController:
  def index(self):
    items = Item.all()

    view = ItemsView(Item.FIELDS, items)
    view.render()


  def new(self):
    attrs = {
      'name': input('Введите фамилию и инициалы: '),
      'phone': input('Введите номер телефона: '),
      'address': input('Введите адрес: '),
    }

    item = Item(attrs)
    item.create()

    view = NewItemView(item)
    view.render()

    # redirect to
    self.index()


  def edit(self):
    id = int(input('Введите № записи: '))
    item = Item.find(id)

    if item:
      attrs = {
        'name': input(f'Введите фамилию и инициалы [{item.name}]: '),
        'phone': input(f'Введите номер телефона [{item.phone}]: '),
        'address': input(f'Введите адрес [{item.address}]: '),
      }
      item.update(attrs)

      view = EditItemView(item)
      view.render()
    else:
      self.__not_found()

    # redirect to
    self.index()


  def delete(self):
    id = int(input('Введите № записи: '))
    item = Item.find(id)

    if item:
      item.destroy()

      view = DeleteItemView(item)
      view.render()
    else:
      self.__not_found()

    # redirect to
    self.index()


  def __not_found(self):
    print('\n404 =(\nЗапись не найдена!\n')
