from controllers.main_controller import MainController

from models.department import Department

from views.departments.index import DepartmentsView
from views.departments.new import NewDepartmentView
from views.departments.edit import EditDepartmentView
from views.departments.delete import DeleteDepartmentView

class DepartmentsController(MainController):
  def index(self):
    departments = Department.all()

    view = DepartmentsView(Department.FIELDS, departments)
    view.render()


  def new(self):
    attrs = {
      'title': input('Введите название: '),
    }

    department = Department(attrs)
    department.create()

    view = NewDepartmentView(department)
    view.render()

    # redirect to
    self.index()


  def edit(self):
    id = int(input('Введите № записи: '))
    department = Department.find(id)

    if department:
      attrs = {
        'title': input(f'Введите название [{department.title}]: '),
      }
      department.update(attrs)

      view = EditDepartmentView(department)
      view.render()
    else:
      self.__not_found()

    # redirect to
    self.index()


  def delete(self):
    id = int(input('Введите № записи: '))
    department = Department.find(id)

    if department:
      if department.destroy():
        view = DeleteDepartmentView(department)
        view.render()
    else:
      self.__not_found()

    # redirect to
    self.index()
