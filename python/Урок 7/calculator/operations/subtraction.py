from operations.base import Base

class Subtraction(Base):
  def execute(self):
    return self.first_operand - self.second_operand
