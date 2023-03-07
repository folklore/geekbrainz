from controllers.lottery_controller import LotteryController


class LotteryRouter:
  def __init__(self):
    self.controller = LotteryController()

    self.actions_map = {
      'show': self.controller.show,
      'hoax': self.controller.hoax,
      'take': self.controller.take
    }

  def go(self):
    while True:
      print('Развод и лохотрон или честная лотерея?')
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
