from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.multiplication import Multiplication
from operations.division import Division
from operations.exponentiation import Exponentiation

class Model:
  OPERATIONS_MAP = {
    '+': Addition,
    '-': Subtraction,
    '*': Multiplication,
    '/': Division,
    '^': Exponentiation,
  }


  def __init__(self):
    self.first_operand = None
    self.operation = None
    self.second_operand = None


  def attrs_assign(self, phrase):
    split_phrase = phrase.split(' ')

    self.first_operand = float(split_phrase[0])
    self.operation = split_phrase[1]
    self.second_operand = float(split_phrase[2])


  def call(self):
    operation = self.OPERATIONS_MAP[self.operation](self.first_operand, self.second_operand)
    result = operation.execute()
    return result
