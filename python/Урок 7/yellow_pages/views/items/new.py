class NewItemView:
  def __init__(self, item):
    self.item = item


  def render(self):
    print(f'Запись № {self.item.id} успешно добавлена!')
