class ItemsView:
  def __init__(self, items):
    self.items = items


  def render(self):
    table_head = ' | '.join([
      self.items['fields']['id'].center(3),
      self.items['fields']['name'].center(20),
      self.items['fields']['phone'].center(12),
      self.items['fields']['address'].center(40)
    ])

    print(table_head)

    for item in self.items['collection']:
      table_row = ' | '.join([
        str(item.id).center(3),
        item.name.ljust(20),
        item.phone.ljust(12),
        item.address.ljust(40)
      ])

      print('-' * len(table_row))
      print(table_row)
