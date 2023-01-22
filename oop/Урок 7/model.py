from models.attrs_assign import AttrsAssign

class Model:
  def __init__(self):
    self.first_operand = None
    self.operation = None
    self.second_operand = None


  def attrs_assign(self, phrase):
    AttrsAssign(self).call(phrase)
