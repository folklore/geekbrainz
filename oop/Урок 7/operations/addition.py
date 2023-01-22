from operations.base import Base

class Addition(Base):
  def execute(self):
    return self.first_operand + self.second_operand
