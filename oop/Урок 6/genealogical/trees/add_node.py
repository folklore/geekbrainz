# Taken out of the Tree class
#   Single Responsibility Principle

from genealogical.nodes.male import Male
from genealogical.nodes.female import Female

class AddNode():
    NODES_MAP = {
        Male.sex: Male,
        Female.sex: Female,
    }


    def __init__(self, tree):
        self.tree = tree


    def call(self):
        commands = "; ".join([f"{i + 1}: {n}" for i, n in enumerate(self.NODES_MAP.keys())])
        sex_number = int(input(f'\nУкажите пол ({commands}): ')) - 1

        Node = list(self.NODES_MAP.values())[sex_number]

        name = input('Введите имя: ')
        node = Node(name)

        self.tree.nodes.append(node)
