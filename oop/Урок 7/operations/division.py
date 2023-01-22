from operations.base import Base

class Division(Base):
  def execute(self):
    return self.first_operand / self.second_operand
