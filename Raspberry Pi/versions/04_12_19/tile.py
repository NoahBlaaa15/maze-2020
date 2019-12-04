#maze 2020 tile library
import data_storage

class Tile:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.type = 'standard'
        self.visited = False


    def set_type(self, tpe):
        self.type = tpe
    #Typisierung der Platte -> Standard, Black(Gulag), Checkpoint, Debris, Ramp

    def __str__(self):
        return "Tile at " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "."

    def __repr__(self):
        return "Tile at " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "."

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited
