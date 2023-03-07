from controllers.toy_controller import ToyController


class ToyRouter:
  def __init__(self):
    self.controller = ToyController()

    self.actions_map = {
      'index': self.controller.index,
      'new': self.controller.new,
      'edit': self.controller.edit,
      'delete': self.controller.delete
    }

  def go(self):
    while True:
      print('Склад игрушек')
      print('')
      print(f'Возможные действия [return]: ``, `{"`, `".join(self.actions_map.keys())}`, `return`')
      command = input('Введите действие: ')
      print('')

      if command in self.actions_map.keys():
        self.actions_map[command]()

      elif command == 'return' or command == '':
        break
      else:
        print('Укажите действие из списка')
