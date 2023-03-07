from controllers.home_controller import HomeController


class HomeRouter:
  def __init__(self):
    pass

  def go(self):
    controller = HomeController()
    controller.index()
