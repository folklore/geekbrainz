from genealogical.node import Node 

class Female(Node):
    sex = 'female'


    def pronoun(self):
        return 'её'
