from controllers.main_controller import MainController

from models.employee import Employee

from views.employees.index import EmployeesView
from views.employees.new import NewEmployeeView
from views.employees.edit import EditEmployeeView
from views.employees.delete import DeleteEmployeeView

class EmployeesController(MainController):
  def index(self):
    employees = Employee.all()

    view = EmployeesView(Employee.FIELDS, employees)
    view.render()


  def new(self):
    attrs = {
      'name': input('Введите фамилию и инициалы: '),
      'phone': input('Введите номер телефона: '),
      'department_id': self.__department_id_input(),
    }

    employee = Employee(attrs)
    employee.create()

    view = NewEmployeeView(employee)
    view.render()

    # redirect to
    self.index()


  def edit(self):
    id = int(input('Введите № записи: '))
    employee = Employee.find(id)

    if employee:
      attrs = {
        'name': input(f'Введите фамилию и инициалы [{employee.name}]: '),
        'phone': input(f'Введите номер телефона [{employee.phone}]: '),
        'department_id': self.__department_id_input(employee.department_id),
      }
      employee.update(attrs)

      view = EditEmployeeView(employee)
      view.render()
    else:
      self.__not_found()

    # redirect to
    self.index()


  def delete(self):
    id = int(input('Введите № записи: '))
    employee = Employee.find(id)

    if employee:
      if employee.destroy():
        view = DeleteEmployeeView(employee)
        view.render()
    else:
      self.__not_found()

    # redirect to
    self.index()


  def __department_id_input(self, department_id = ''):
    if department_id == '':
      text = f'Введите номер подразделения: '
    else:
      text = f'Введите номер подразделения [{department_id}]: '

    new_id = input(text)

    if new_id == '':
      if department_id != '':
        return department_id
      else:
        print('Номер подразделения не может быть пустым!')
        return self.__department_id_input(department_id)
    else:
      return int(new_id)
