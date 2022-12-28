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
    return collection


  @classmethod
  def find(klass, id):
    if id in klass.__ids(klass):
      item = klass.__raw_find(klass, id)
      return klass(item)


  def __init__(self, attrs):
    self.id = attrs.get('id')

    self.name = attrs['name']
    self.phone = attrs['phone']
    self.address = attrs['address']


  def create(self):
    self.id = max(self.__ids()) + 1

    self.storage.append({
      'id': self.id,
      'name': self.name,
      'phone': self.phone,
      'address': self.address,
    })


  def update(self, attrs):
    item = self.__raw_find(self.id)

    for key in ['name', 'phone', 'address']:
      if attrs[key]:
        item[key] = attrs[key]


  def destroy(self):
    Item.storage = [item for item in self.storage if item['id'] != self.id]


  def __raw_find(self, id):
    return next(item for item in self.storage if item['id'] == id)


  def __ids(self):
    return [item['id'] for item in self.storage]
