# Taken out of the Tree class
#   Single Responsibility Principle

class Show():
    def __init__(self, tree):
        self.tree = tree


    def call(self):
        print('\nТекущие данные ГД:\n')

        if(len(self.tree.nodes) > 0):
            for index, node in enumerate(self.tree.nodes):
                print(f'  {index + 1} | {node.show()}')
        else:
            print('Пусто.')
