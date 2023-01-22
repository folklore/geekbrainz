from model import Model
from view import View
from controller import Controller

model = Model()
controller = Controller(model)

view = View()
controller.run(view)
