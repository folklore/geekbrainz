class Edge():
    RELATIONSHIPS = [
        'husband',
        'wife',
        'parent',
        'child',
    ]


    def __init__(self, relationship, node, reverse=False):
        self.node = node

        if(reverse):
            self.relationship = self.__revese_relationship(relationship)
        else:
            self.relationship = relationship


    # Public.
    def info(self):
        if(self.relationship == 'husband'):
            text = 'жена'
        elif(self.relationship == 'wife'):
            text = 'муж'
        elif(self.relationship == 'parent'):
            text = 'отец' if(self.node.sex == 'male') else 'мать'
        elif(self.relationship == 'child'):
            text = 'сын' if(self.node.sex == 'male') else 'дочь'
        return f'{text} {self.node.name}'


    # Internal.
    def __revese_relationship(self, relationship):
        if(relationship == 'husband'):
            return 'wife'
        if(relationship == 'wife'):
            return 'husband'
        if(relationship == 'parent'):
            return 'child'
        if(relationship == 'child'):
            return 'parent'
