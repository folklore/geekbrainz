from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.multiplication import Multiplication
from operations.division import Division
from operations.exponentiation import Exponentiation


class Calculator():
  OPERATIONS_MAP = {
    '+': Addition,
    '-': Subtraction,
    '*': Multiplication,
    '/': Division,
    '^': Exponentiation,
  }


  def __init__(self, model):
    self.model = model


  def execute(self):
    operation = self.OPERATIONS_MAP[self.model.operation](self.model.first_operand, self.model.second_operand)
    result = operation.execute()
    return result
