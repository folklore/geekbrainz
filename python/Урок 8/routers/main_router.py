from controllers.main_controller import MainController

class MainRouter():
  def __init__(self):
      self.controller = MainController()


  def go(self):
    self.controller.index()
