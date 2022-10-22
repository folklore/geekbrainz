from views.main.index import MainView

class MainController:
  def index(self):
    view = MainView()
    view.render()


  def __not_found(self):
    print('\n404 =(\nЗапись не найдена!\n')
