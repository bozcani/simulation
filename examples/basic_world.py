from simulation.environment import Environment
from simulation.observer import Observer
from simulation.models import Model


o = Observer(0,0,0,0,0)
car_1 = Model(0, "car", 2, 1)
car_2 = Model(1, "car", 2, 1)
car_3 = Model(2, "car", 2, 1.5)



e = Environment()

e.add_object(car_1, x=2, y=3, theta=4, Vx=4, angularZ=4)
e.add_object(car_2, x=7, y=3, theta=4, Vx=0, angularZ=0)
e.add_object(car_3, x=4, y=7, theta=4, Vx=0, angularZ=0)

e.add_observer(o)

e.print_objects()

e.observe()