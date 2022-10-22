class EmployeesView:
  def __init__(self, fields, employees):
    self.fields = fields
    self.employees = employees


  def render(self):
    table_head = ' | '.join([
      self.fields['id'].center(3),
      self.fields['name'].center(20),
      self.fields['phone'].center(12),
      'Подразделение'.center(40)
    ])

    print(table_head)

    for employee in self.employees:
      table_row = ' | '.join([
        str(employee.id).center(3),
        employee.name.ljust(40),
        employee.phone.ljust(12),
        employee.department().title.ljust(20)
      ])

      print('-' * len(table_row))
      print(table_row)
