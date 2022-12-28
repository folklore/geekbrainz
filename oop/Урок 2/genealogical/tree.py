from genealogical.edge import Edge

from genealogical.nodes.male import Male
from genealogical.nodes.female import Female

from genealogical.analysis import Analysis


class Tree():
    NODES_MAP = {
        Male.sex: Male,
        Female.sex: Female,
    }


    def __init__(self):
        self.nodes = []

        self.actions_map = {
            'build': self.build,
            'analysis': self.analysis,
            'show': self.show,
            'add_node': self.add_node,
            'add_edge': self.add_edge,
        }


    def build(self):
        print('\nДобавление данных в ГД:')

        self.add_node()
        self.add_node()
        self.show()
        self.add_edge()
        self.show()


    def show(self):
        print('\nТекущие данные ГД:\n')

        if(len(self.nodes) > 0):
            for index, node in enumerate(self.nodes):
                print(f'  {index + 1} | {node.show()}')
        else:
            print('Пусто.')


    def add_node(self):
        commands = "; ".join([f"{i + 1}: {n}" for i, n in enumerate(self.NODES_MAP.keys())])
        sex_number = int(input(f'\nУкажите пол ({commands}): ')) - 1

        Node = list(self.NODES_MAP.values())[sex_number]

        name = input('Введите имя: ')
        node = Node(name)

        self.nodes.append(node)


    def add_edge(self):
        node_one_number = int(input(f'\nВыберите первого человека (от 1 до {len(self.nodes)}): ')) - 1
        node_one = self.nodes[node_one_number]

        commands = "; ".join([f"{i + 1}: {r}" for i, r in enumerate(Edge.RELATIONSHIPS)])
        rel_number = int(input(f'Укажите отношения ({commands}): ')) - 1

        rel = Edge.RELATIONSHIPS[rel_number]

        node_two_number = int(input(f'Выберите второго человека (от 1 до {len(self.nodes)}): ')) - 1
        node_two = self.nodes[node_two_number]

        node_one.edges.append(Edge(rel, node_two))
        node_two.edges.append(Edge(rel, node_one, reverse=True))


    # Без особой защиты от цикличности "графа".
    #
    def analysis(self):
        id = int(input(f'\nВыберите человека (от 1 до {len(self.nodes)}): ')) - 1
        node = self.nodes[id]
        print('')

        Analysis(node).run()
