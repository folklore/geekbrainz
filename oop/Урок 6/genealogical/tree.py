from genealogical.trees.show import Show

from genealogical.trees.add_node import AddNode
from genealogical.trees.add_edge import AddEdge

from genealogical.trees.analysis import Analysis


class Tree():
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
        Show(self).call()


    def add_node(self):
        AddNode(self).call()


    def add_edge(self):
        AddEdge(self).call()


    def analysis(self):
        Analysis(self).call()
