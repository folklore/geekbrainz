from routers.main_router import MainRouter
from routers.departments_router import DepartmentsRouter
from routers.employees_router import EmployeesRouter

main_router = MainRouter()
print('')
main_router.go()

routing = {
  'main': main_router,
  'departments': DepartmentsRouter(),
  'dep': DepartmentsRouter(),
  'employees': EmployeesRouter(),
  'emp': EmployeesRouter(),
}

while True:
  print('\nВозможные действия: "main", "departments", "dep", "employees", "emp", "exit"')
  route = input('Введите действие: ')
  print('')

  if route in routing.keys():
    router = routing[route]
    router.go()

  elif route == 'exit':
    exit()
  else:
    print('Укажите действие из списка')
