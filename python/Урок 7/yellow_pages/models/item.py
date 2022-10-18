import collections


class Item:
  FIELDS = {
    'id': '№',
    'name': 'Фамилия И.О.',
    'phone': 'Телефон',
    'address': 'Адрес',
  }

  storage = [
    {
      'id': 1,
      'name': 'Пушкин А.С.',
      'phone': '+74956941289',
      'address': 'Тверской бульвар, дом 23',
    },
    {
      'id': 2,
      'name': 'Маяковский В.В.',
      'phone': '+74956904232',
      'address': 'Большая Никитская, дом 19/13',
    },
  ]

  @classmethod
  def all(klass):
    collection = [klass(item) for item in klass.storage]

    return {
      'fields': klass.FIELDS,
      'collection': collection
    }


  def __init__(self, attrs):
    self.id = attrs['id']
    self.name = attrs['name']
    self.phone = attrs['phone']
    self.address = attrs['address']


  def save(self):
    self.id = len(self.storage) + 1

    self.storage.append({
      'id': self.id,
      'name': self.name,
      'phone': self.phone,
      'address': self.address,
    })
