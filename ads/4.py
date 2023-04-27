from termcolor import colored

class Tree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.red = True

            self.left = None
            self.right = None
            self.parent = None

    def insert(self, value):
        node = self.Node(value)

        if self.root is None:
            node.red = False
            self.root = node
            print('ROOT IS - {}'.format(self.root.key))
            return

        last_node = self.root

        while last_node is not None:
            potential_parent = last_node

            if node.key < last_node.key:
                last_node = last_node.left
            else:
                last_node = last_node.right

        node.parent = potential_parent
        print('NODE KEY- {} NODE PARENT - {} '.format(node.key,
                                                      node.parent.key))

        if node.key < node.parent.key:
            node.parent.left = node
            print('GO LEFT < NODE PARENT PARENT LEFT KEY - ',
                  node.parent.key)
        else:
            node.parent.right = node
            print('GO RIGHT > NODE PARENT PARENT RIGHT KEY - ',
                  node.parent.key)

        node.left = None
        node.right = None

        self.fix_tree(node)


    def fix_tree(self, node):
        print('NODE PARENT RED - {}'.format(node.parent.red))

        try:
            while node.parent.red is True and node is not self.root:
                print('FIX>> NODE KEY - {} '
                      'NODE PARENT KEY - {} '.format(node.key,
                                                     node.parent.key))
                if node.parent == node.parent.parent.left:
                    uncle = node.parent.parent.right
                    print('[LEFT] UNCLE RED - {} '
                          'UNCLE KEY - {} PARENT PARENT {}'.format(uncle.red, uncle.key, node.parent.parent.key))

                    if uncle.red:
                        node.parent.red = False
                        uncle.red = False
                        node.parent.parent.red = True
                        node = node.parent.parent
                        print('NODE RED - {} UNCLE RED - {} PARENT RED - '
                              '{}'.format(
                                    colored(node.red, 'red',
                                            attrs=['reverse', 'blink']),
                                    colored(uncle.red, 'yellow',
                                            attrs=['reverse', 'blink']),
                                    colored(node.parent.red, 'yellow',
                                            attrs=['reverse', 'blink'])))
                    else:
                        if node == node.parent.right:
                            print('in TEST>>>>', node.key)
                            node = node.parent
                            print('AFTER TEST>>>>', node.key)
                else:
                    try:
                        uncle = node.parent.parent.left
                        print('[RIGHT] UNCLE RED - {} '
                              'UNCLE KEY - {}'.format(uncle.red, uncle.key))
                        if uncle.red:
                            node.parent.red = False
                            uncle.red = False
                            node.parent.parent.red = True
                            print('NODE RED - {} UNCLE RED - {} PARENT RED - '
                                  '{}'.format(
                                        colored(node.red, 'red',
                                                attrs=['reverse', 'blink']),
                                        colored(uncle.red, 'yellow',
                                                attrs=['reverse', 'blink']),
                                        colored(node.parent.red, 'yellow',
                                                attrs=['reverse', 'blink'])))

                    except AttributeError:
                        print("DOES NOT GAVE UNCLE")
                        break

            self.root.red = False
        except AttributeError:
            print("\n\nTree BUILT")
