from routers.home_router import HomeRouter
from routers.lottery_router import LotteryRouter
from routers.toy_router import ToyRouter


routers_map = {
  'home': HomeRouter(),
  'lottery': LotteryRouter(),
  'toy': ToyRouter(),
}

routers_map['home'].go()


while True:
  print(f'Возможные действия [exit]: ``, `{"`, `".join(routers_map.keys())}`, `exit`')
  command = input('Введите действие: ')
  print('')

  if command in routers_map.keys():
    router = routers_map[command]
    router.go()

  elif command == 'exit' or command == '':
    print('Всего доброго!')

    exit()
  else:
    print('Укажите действие из списка')
