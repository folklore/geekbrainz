from abc import ABC, abstractmethod


# Public. Abstract class.
class Base(ABC):
    def __init__(self, name):
        self.name = name
        self.edges = []


    def show(self):
        if(len(self.edges) == 0):
            return f'{self.name}'
        else:
            relationships = [edge.info() for edge in self.edges]
            return f'{self.name}, {self.pronoun()} {", ".join(relationships)}'


    @abstractmethod
    def pronoun(self):
        pass
