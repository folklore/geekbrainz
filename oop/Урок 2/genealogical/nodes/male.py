from genealogical.nodes.base import Base 


class Male(Base):
    sex = 'male'


    def pronoun(self):
        return 'его'
