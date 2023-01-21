class Edge():
    RELATIONSHIPS_MAP = {
        'husband': 'wife',
        'wife': 'husband',
        'parent': 'child',
        'child': 'parent',
    }


    def __init__(self, relationship, node, reverse=False):
        self.node = node

        if(reverse):
            self.relationship = self.RELATIONSHIPS_MAP[relationship]
        else:
            self.relationship = relationship


    # Public.
    def info(self):
        if(self.relationship == 'husband'):
            text = 'жена'
        elif(self.relationship == 'wife'):
            text = 'муж'
        elif(self.relationship == 'parent' and self.node.sex == 'male'):
            text = 'отец'
        elif(self.relationship == 'parent' and self.node.sex == 'female'):
            text = 'мать'
        elif(self.relationship == 'child' and self.node.sex == 'male'):
            text = 'сын'
        elif(self.relationship == 'child' and self.node.sex == 'female'):
            text = 'дочь'
        else:
            text = 'н/д'
        return f'{text} {self.node.name}'
