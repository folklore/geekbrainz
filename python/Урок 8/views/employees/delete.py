class DeleteEmployeeView:
  def __init__(self, employee):
    self.employee = employee


  def render(self):
    print(f'\nЗапись № {self.employee.id} успешно удалена!\n')
