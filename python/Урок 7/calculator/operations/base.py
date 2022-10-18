class Base:
  def __init__(self, first_operand, second_operand):
    self.first_operand = first_operand
    self.second_operand = second_operand

  def execute(self):
    raise NotImplementedError('Метод должен быть определен в дочерних классах')
