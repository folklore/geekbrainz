from storage import Storage

from random import randint as RandInt

from views.lottery.show_view import ShowView
from views.lottery.hoax_view import HoaxView
from views.lottery.take_view import TakeView


class LotteryController:
  def __init__(self):
    self.storage = Storage()


  def show(self):
    toy_titles = self.storage.issued()

    view = ShowView(toy_titles)
    view.render()


  def hoax(self):
    toys = sorted(self.storage.all(), key=lambda toy:toy.frequency)

    view = HoaxView()

    for toy in toys:
      random_frequency = RandInt(1, 100)

      if(random_frequency <= toy.frequency):
        self.storage.issue(toy)
        view.render_gain(toy)
        return

    view.render_pain()


  def take(self):
    toy_titles = self.storage.issued()

    view = TakeView(toy_titles)
    view.render()

    self.storage.clean_issued()
