import csv
from models.toy import Toy


class Storage():
  STORAGE_FILE = 'storage.csv'
  ISSUANCE_FILE = 'issuance.txt'


  def __init__(self):
    pass


  def all(self):
    with open(self.STORAGE_FILE, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
      return [Toy(index+1, *params) for index, params in enumerate(reader)]


  def clean(self):
    storage = open(self.STORAGE_FILE, "w+")
    storage.close()


  def save(self, toy):
    with open(self.STORAGE_FILE, 'a', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
      writer.writerow(self.__to_csv(toy))


  def issue(self, won_toy):
    toys = self.all()
    self.clean()

    for toy in toys:
      if won_toy.id == toy.id:
        toy.count = toy.count - 1
      self.save(toy)

    with open(self.ISSUANCE_FILE, 'a') as txtfile:
      txtfile.write(won_toy.title)
      txtfile.write('\n')


  def issued(self):
    with open(self.ISSUANCE_FILE) as txtfile:
      return [toy_title.rstrip() for toy_title in txtfile]


  def clean_issued(self):
    txtfile = open(self.ISSUANCE_FILE, "w+")
    txtfile.close()


  def __to_csv(self, toy):
    return [toy.title, toy.count, toy.frequency]
