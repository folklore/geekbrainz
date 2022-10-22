class Employee:
  FIELDS = {
    'id': '№',
    'name': 'Фамилия И.О.',
    'phone': 'Телефон',
    'department_id': 'Подразделение',
  }

  storage = [
    {
      'id': 1,
      'name': 'Остап Сулейман Берта Мария Бендер-бей',
      'phone': '111-11-11',
      'department_id': 1,
    },
    {
      'id': 2,
      'name': 'Паниковский Михаил Самуэлевич',
      'phone': '222-11-22',
      'department_id': 2,
    },
    {
      'id': 3,
      'name': 'Шура Балаганов',
      'phone': '222-33-22',
      'department_id': 2,
    },
  ]


  @classmethod
  def all(klass):
    collection = [klass(employee) for employee in klass.storage]
    return collection


  @classmethod
  def find(klass, id):
    if id in klass.__ids(klass):
      employee = klass.__raw_find(klass, id)
      return klass(employee)


  def __init__(self, attrs):
    self.id = attrs.get('id')

    self.name = attrs['name']
    self.phone = attrs['phone']
    self.department_id = attrs['department_id']


  def department(self):
    from models.department import Department

    if self.department_id:
      departments = Department.all()
      return next(department for department in departments if department.id == self.department_id)
    else:
      Department({'title': ''})


  def create(self):
    self.id = max(self.__ids()) + 1

    self.storage.append({
      'id': self.id,
      'name': self.name,
      'phone': self.phone,
      'department_id': self.department_id,
    })


  def update(self, attrs):
    employee = self.__raw_find(self.id)

    for key in ['name', 'phone', 'department_id']:
      if attrs[key]:
        employee[key] = attrs[key]


  def destroy(self):
    Employee.storage = [employee for employee in self.storage if employee['id'] != self.id]
    return True

  def __raw_find(self, id):
    return next(employee for employee in self.storage if employee['id'] == id)


  def __ids(self):
    return [employee['id'] for employee in self.storage]
