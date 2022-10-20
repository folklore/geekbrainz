from controllers.items_controller import ItemsController
from controllers.items.export_controller import ExportItemsController
from controllers.items.import_controller import ImportItemsController

items_controller = ItemsController()
print('')
items_controller.index()

while True:
  print('\nВозможные действия: "index", "new", "edit". TODO "export", "import".')
  route = input('Введите действие: ')
  print('')

  if route == 'index':
    items_controller.index()

  elif route == 'new':
    items_controller.new()

  elif route == 'edit':
    items_controller.edit()

  elif route == 'export':
    export_items_controller = ExportItemsController()
    export_items_controller.run()

  elif route == 'import':
    import_items_controller = ImportItemsController()
    import_items_controller.run()

  else:
    print('Укажите действие из списка')
