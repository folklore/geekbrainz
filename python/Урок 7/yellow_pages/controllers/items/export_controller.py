from models.item import Item
from services.items.export_service import ExportItemsService

class ExportItemsController:
  def run(self):
    filename = int(input('Введите имя json файла: '))

    export_items_service = ExportItemsService(filename)
    export_items_service.call()
