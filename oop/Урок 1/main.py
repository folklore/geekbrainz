from genealogical.tree import Tree

print('Добро пожаловать в сервис "формирования" генеалогического древа (далее - ГД)!')

tree = Tree()
tree.show()
tree.build()

while(True):
    commands = f'{"; ".join([f"{i + 1}: {n}" for i, n in enumerate(tree.actions_map.keys())])}, {len(tree.actions_map) + 1}: exit'
    command_number = int(input(f'\nВведите команду ({commands}): ')) - 1

    if(command_number < len(tree.actions_map)):
        list(tree.actions_map.values())[command_number]()
    elif(command_number == 5):
        print('\nВсего доброго!\n')
        break
    else:
        print('Нет такой команды.')
