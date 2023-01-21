# Taken out of the Tree class
#   Single Responsibility Principle

from genealogical.edge import Edge

class AddEdge():
    def __init__(self, tree):
        self.tree = tree


    def call(self):
        node_one_number = int(input(f'\nВыберите первого человека (от 1 до {len(self.tree.nodes)}): ')) - 1
        node_one = self.tree.nodes[node_one_number]

        commands = "; ".join([f"{i + 1}: {r}" for i, r in enumerate(list(Edge.RELATIONSHIPS_MAP.keys()))])
        rel_number = int(input(f'Укажите отношения ({commands}): ')) - 1

        rel = list(Edge.RELATIONSHIPS_MAP.keys())[rel_number]

        node_two_number = int(input(f'Выберите второго человека (от 1 до {len(self.tree.nodes)}): ')) - 1
        node_two = self.tree.nodes[node_two_number]

        node_one.edges.append(Edge(rel, node_two))
        node_two.edges.append(Edge(rel, node_one, reverse=True))
