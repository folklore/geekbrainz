class DepartmentsView:
  def __init__(self, fields, departments):
    self.fields = fields
    self.departments = departments


  def render(self):
    table_head = ' | '.join([
      self.fields['id'].center(3),
      self.fields['title'].center(20),
      'Сотрудники'.center(40)
    ])

    print(table_head)

    for department in self.departments:
      table_row = ' | '.join([
        str(department.id).center(3),
        department.title.ljust(20),
        (', ').join([employee.name for employee in department.employees()]).ljust(40)
      ])

      print('-' * len(table_row))
      print(table_row)
