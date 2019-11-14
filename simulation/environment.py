from simulation.models import Model
import math

class Environment:
    def __init__ (self, size=(500, 500)):
        self.objects = []
        self.observer = None

    def add_object(self, model, x, y, theta,Vx,angularZ ):    
        self.objects.append(Object(model, x,y,theta,Vx,angularZ))

    def add_observer(self, observer):
        self.observer = observer    

    def observe(self, area=(16,16)):
        print("Observing...")
        print(self.observer)

        lim_x, lim_y = area

        x, y = self.observer.x, self.observer.y

        # Get the observable objects around the observer.
        observable_objs = []
        for obj in self.objects:
            ox, oy = obj.x, obj.y
            if ox>x-(lim_x/2) and ox<x+(lim_x/2):
                if oy>y-(lim_y/2) and oy<y+(lim_y/2):
                    observable_objs.append(obj)

        print("Observed objects:")
        #for o in observable_objs:
        #    print(o)            

        #M = [row for row in]

        theta = (math.radians(self.observer.orientation))

        for j in range(lim_x):
            for i in range(lim_y):
                skip=0
                for o in observable_objs:

                    # Add rotation
                    ox = math.cos(theta)*o.x-math.sin(theta)*o.y
                    oy = math.sin(theta)*o.x+math.cos(theta)*o.y

                    r_x, r_y = int(ox-(self.observer.x-(lim_x/2))), int(oy-(self.observer.y-(lim_y/2)))
                    if r_x==j and r_y==i:
                        print(o.model.id, end=' ')
                        skip = 1
                if skip==0:
                    print('x', end=' ')        

            print()
        


    def print_objects(self):
        for o in self.objects:
            print(o)    


    def tick(self):
        """ Move objects and observer according to the their velocities. """
        
        # Turn the observer.
        self.observer.orientation += self.observer.angular_Z

        # Translate the observer.
        theta = (math.radians(self.observer.orientation))
        self.observer.x += math.cos(theta)*self.observer.linear_X
        self.observer.y += math.sin(theta)*self.observer.linear_X

        for obj in self.objects:
            # Turn the object.
            obj.theta += obj.angular_Z

            # Move the object.
            theta = (math.radians(obj.theta))
            obj.x += math.cos(theta)*obj.linear_X
            obj.y += math.sin(theta)*obj.linear_X

class Object:
    def __init__(self, model, x, y, theta, linear_X, angular_Z):
        self.model = model
        self.x = x
        self.y = y
        self.theta = theta
        self.linear_X = linear_X
        self.angular_Z = angular_Z  

    def __str__(self):
        info = "Object -> (x,y)=("+str(self.x)+", "+str(self.y)+'), '
        info += "ori: "+str(self.theta)+", "
        info += "Vx: "+str(self.linear_X)+", "
        info += "angular_Z: "+str(self.angular_Z)
        info += ", which is "+str(self.model)
        return info              