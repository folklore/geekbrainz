from controllers.departments_controller import DepartmentsController

class DepartmentsRouter():
  def __init__(self):
      self.controller = DepartmentsController()

      self.actions = {
        '': self.controller.index,
        'index': self.controller.index,
        'new': self.controller.new,
        'edit': self.controller.edit,
        'delete': self.controller.delete,
      }

  def go(self):
    while True:
      print('\nВыбрана работа с подразделениями')
      print('Возможные действия [index]: "index", "new", "edit", "delete", "return"')
      route = input('Введите действие: ')
      print('')

      if route in self.actions.keys():
        self.actions[route]()

      elif route == 'return':
        break
      else:
        print('Укажите действие из списка')
