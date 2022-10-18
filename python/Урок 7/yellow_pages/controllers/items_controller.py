from models.item import Item

from views.items.index import ItemsView
from views.items.new import NewItemView
from views.items.edit import EditItemView

class ItemsController:
  def index(self):
    items = Item.all()

    view = ItemsView(items)
    view.render()


  def new(self):
    attrs = {
      'id': None,
      'name': input('Введите фамилию и инициалы: '),
      'phone': input('Введите номер телефона: '),
      'address': input('Введите адрес: '),
    }

    item = Item(attrs)
    item.save()

    view = NewItemView(item)
    view.render()


  def edit(self):
    number = int(input('Введите № записи: '))
