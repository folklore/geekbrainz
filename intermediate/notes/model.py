from datetime import datetime
import csv

class Model():
  TIMESTAMP_FORMAT = '%d.%m.%Y %H:%M:%S'
  STORAGE_FILE = 'storage.csv'

  def __init__(self, title, body, timestamp=datetime.now().strftime(TIMESTAMP_FORMAT)):
    self.title = title
    self.body = body
    self.timestamp = datetime.strptime(timestamp, self.TIMESTAMP_FORMAT)


  def to_csv(self):
    return [self.title, self.body, self.pretty_timestamp()]


  def to_row(self, index):
    return f' {str(index+1).rjust(2, " ")} | {self.title.ljust(20, " ")} | {self.body.ljust(38, " ")} | {self.pretty_timestamp()}'


  def pretty_timestamp(self):
    return self.timestamp.strftime(self.TIMESTAMP_FORMAT)


  @classmethod
  def all(klass):
    with open(klass.STORAGE_FILE, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
      return [klass(*params) for params in reader]


  @classmethod
  def clean(klass):
    storage = open(klass.STORAGE_FILE, "w+")
    storage.close()


  def save(self):
    with open(self.STORAGE_FILE, 'a', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
      writer.writerow(self.to_csv())


  def touch(self):
    self.timestamp = datetime.now()
