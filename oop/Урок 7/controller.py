from calculator import Calculator

class Controller:
  def __init__(self, model):
    self.model = model


  def run(self, view):
    view.render_greet()

    while True:
      phrase = view.render_input()

      self.model.attrs_assign(phrase)

      result = Calculator(self.model).execute()
      view.render_result(result)
