class Analysis():
    def __init__(self, node):
        self.node = node


    def run(self):
        print(self.node.name)

        def recur(edges, indent):
            for edge in edges:
                if(edge.node == self.node):
                    break
                print(f'{" " * indent}{edge.info()}')

                recur(edge.node.edges, indent + 2)

        recur(self.node.edges, 2)
