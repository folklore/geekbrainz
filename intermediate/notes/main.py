from actions.index_action import IndexAction
from actions.filter_action import FilterAction
from actions.new_action import NewAction
from actions.show_action import ShowAction
from actions.edit_action import EditAction
from actions.delete_action import DeleteAction

actions_map = {
  'index': IndexAction(),
  'filter': FilterAction(),
  'new': NewAction(),
  'show': ShowAction(),
  'edit': EditAction(),
  'delete': DeleteAction(),
}

actions_map['index'].call()

while True:
  print(f'Возможные действия: {", ".join(actions_map.keys())}, exit')
  command = input('Введите действие: ')
  print('')

  if command in actions_map.keys():
    action = actions_map[command]
    action.call()

  elif command == 'exit':
    print('Всего доброго!')

    exit()
  else:
    print('Укажите действие из списка')
