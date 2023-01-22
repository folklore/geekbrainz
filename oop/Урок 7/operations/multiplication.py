from operations.base import Base

class Multiplication(Base):
  def execute(self):
    return self.first_operand * self.second_operand
