from genealogical.nodes.base import Base 


class Female(Base):
    sex = 'female'


    def pronoun(self):
        return 'её'
