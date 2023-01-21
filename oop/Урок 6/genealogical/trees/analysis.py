# Taken out of the Tree class
#   Single Responsibility Principle

class Analysis():
    def __init__(self, tree):
        self.tree = tree


    def call(self):
        id = int(input(f'\nВыберите человека (от 1 до {len(self.tree.nodes)}): ')) - 1
        node = self.tree.nodes[id]
        print('')
        print(node.name)

        def recur(edges, indent):
            for edge in edges:
                if(edge.node == node):
                    break
                print(f'{" " * indent}{edge.info()}')

                recur(edge.node.edges, indent + 2)

        recur(node.edges, 2)
