class AttrsAssign():
  def __init__(self, model):
    self.model = model


  def call(self, phrase):
    split_phrase = phrase.split(' ')

    self.model.first_operand = float(split_phrase[0])
    self.model.operation = split_phrase[1]
    self.model.second_operand = float(split_phrase[2])
