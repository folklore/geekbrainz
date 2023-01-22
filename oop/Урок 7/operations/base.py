from abc import ABC, abstractmethod


# Public. Abstract class.
class Base(ABC):
  def __init__(self, first_operand, second_operand):
    self.first_operand = first_operand
    self.second_operand = second_operand

  @abstractmethod
  def execute(self):
    raise NotImplementedError('Метод должен быть определен в дочерних классах')
