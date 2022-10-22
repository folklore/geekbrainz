class EditDepartmentView:
  def __init__(self, department):
    self.department = department


  def render(self):
    print(f'\nЗапись № {self.department.id} успешно обновлена!\n')
