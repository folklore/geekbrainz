class IndexView:
  def __init__(self, toys):
    self.toys = toys


  def render(self):
    print('Список игрушек')
    print('')

    self.__print_headers()
    self.__print_rows()

    print('')


  def __print_headers(self):
    print(' ## |       Название       | Кол., шт. | Частота выпадания, % ')


  def __print_rows(self):
    for toy in self.toys:
      print(self.__pretty_row(toy))


  def __pretty_row(self, toy):
    return f' {str(toy.id).rjust(2, " ")} | {toy.title.ljust(20, " ")} | {str(toy.count).ljust(9, " ")} | {str(toy.frequency)}'
