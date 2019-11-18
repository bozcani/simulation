from simulation.environment import Environment
from simulation.observer import Observer
from simulation.models import Model

# Create an environment.
e = Environment()

# Create an observer.
o = Observer(0,0,0,linear_X=0,angular_Z=0)

# Create models.
car_1 = Model(0, "car", 2, 1)
car_2 = Model(1, "car", 2, 1)
car_3 = Model(2, "car", 2, 1.5)


# Add models to the environment.
e.add_object(car_1, x=2, y=3, theta=4, Vx=0.5, angularZ=0)
e.add_object(car_2, x=7, y=3, theta=4, Vx=0, angularZ=0)
e.add_object(car_3, x=6, y=7, theta=4, Vx=0, angularZ=0)

# Add the observer to the environment.
e.add_observer(o)

# Print objects.
e.print_objects()

# Execute the environment with all models.
while True:
    e.observe()
    e.tick()
    input()
