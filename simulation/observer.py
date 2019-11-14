
class Observer:
    """ Observer """

    def __init__(self, x, y, orientation, linear_X, angular_Z):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.linear_X = linear_X
        self.angular_Z = angular_Z

    def __str__(self):
        info = "Observer -> (x,y)=("+str(self.x)+", "+str(self.y)+'), '
        info += "ori: "+str(self.orientation)+", "
        info += "linear_X: "+str(self.linear_X)+", "
        info += "angular_Z: "+str(self.angular_Z)
        return info

