from storage import Storage

from views.toy.index_view import IndexView


class HomeController:
  def __init__(self):
    self.storage = Storage()


  def index(self):
    toys = self.storage.all()

    view = IndexView(toys)
    view.render()
