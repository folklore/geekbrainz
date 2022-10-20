class EditItemView:
  def __init__(self, item):
    self.item = item


  def render(self):
    print(f'\nЗапись № {self.item.id} успешно обновлена!\n')
