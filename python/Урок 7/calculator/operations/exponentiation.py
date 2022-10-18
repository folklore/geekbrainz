from operations.base import Base

class Exponentiation(Base):
  def execute(self):
    return self.first_operand ** self.second_operand
