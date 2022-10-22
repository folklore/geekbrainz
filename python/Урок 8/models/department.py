class Department:
  FIELDS = {
    'id': '№',
    'title': 'Название',
  }

  storage = [
    {
      'id': 1,
      'title': 'Управление',
    },
    {
      'id': 2,
      'title': 'Поддержка',
    },
  ]


  @classmethod
  def all(klass):
    collection = [klass(department) for department in klass.storage]
    return collection


  @classmethod
  def find(klass, id):
    if id in klass.__ids(klass):
      department = klass.__raw_find(klass, id)
      return klass(department)


  def __init__(self, attrs):
    self.id = attrs.get('id')

    self.title = attrs['title']


  def employees(self):
    from models.employee import Employee

    employees = Employee.all()
    return [employee for employee in employees if employee.department_id == self.id]


  def create(self):
    self.id = max(self.__ids()) + 1

    self.storage.append({
      'id': self.id,
      'title': self.title,
    })


  def update(self, attrs):
    department = self.__raw_find(self.id)

    for key in ['title']:
      if attrs[key]:
        department[key] = attrs[key]


  def destroy(self):
    if self.employees() != []:
      print('\nФорин кей констрейн =(\n')
      return False
    else:
      Department.storage = [department for department in self.storage if department['id'] != self.id]
      return True


  def __raw_find(self, id):
    return next(department for department in self.storage if department['id'] == id)


  def __ids(self):
    return [department['id'] for department in self.storage]
