from models.item import Item
from services.items.import_service import ImportItemsService

class ImportItemsController:
  def run(self):
    filename = int(input('Введите имя json файла: '))

    import_items_service = ImportItemsService(filename)
    import_items_service.call()
