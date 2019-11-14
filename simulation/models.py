
class Model:
    def __init__ (self, id, type, length, width):
        self.id = id
        self.type = type

        self.length = length
        self.width = width
        # 2D dimensions
        #self.length = length
        #self.width = width

        # Initial orientation
        #self.orientation = orientation

        # Initial velocities
        #self.linear_X = linear_X
        #self.angular_Z = angular_Z

    def __str__(self):
        info = "Model -> id="+str(self.id)+", type: "+str(self.type)+', '
        info += "length: "+str(self.length)+", "
        info += "width: "+str(self.width)
        return info