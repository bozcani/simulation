from simulation.models import Model

class Environment:
    def __init__ (self, size=(500, 500)):
        self.objects = []
        self.observer = None

    def add_object(self, model, x, y, theta,Vx,angularZ ):    
        self.objects.append(Object(model, x,y,theta,Vx,angularZ))

    def add_observer(self, observer):
        self.observer = observer    

    def observe(self, area=(16,16), grid_size=0.5):
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
        for o in observable_objs:
            print(o)            
        #TODO

        #M = [row for row in]

        for j in range(lim_x):
            for i in range(lim_y):
                skip=0
                for o in observable_objs:
                    r_x, r_y = int(o.x-(self.observer.x-(lim_x/2))), int(o.y-(self.observer.y-(lim_y/2)))
                    if r_x==j and r_y==i:
                        print(o.model.id, end=' ')
                        skip = 1
                if skip==0:
                    print('x', end=' ')        

            print()
        


    def print_objects(self):
        for o in self.objects:
            print(o)    



class Object:
    def __init__(self, model, x, y, theta, Vx, angularZ):
        self.model = model
        self.x = x
        self.y = y
        self.theta = theta
        self.Vx = Vx
        self.angularZ = angularZ  

    def __str__(self):
        info = "Object -> (x,y)=("+str(self.x)+", "+str(self.y)+'), '
        info += "ori: "+str(self.theta)+", "
        info += "Vx: "+str(self.Vx)+", "
        info += "angularZ: "+str(self.angularZ)
        info += ", which is "+str(self.model)
        return info              