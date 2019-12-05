#maze 2020 tile library
import data_storage

class Tile:

    def __init__(self, coords):
        #Those are integers
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

        #Those are 'unknown', 'wall' or 'open'
        self.top = 'unknown'
        self.right = 'unknown'
        self.bot = 'unknown'
        self.left = 'unknown'

        self.type = 'standard'
        self.visited = False

    def set_type(self, parameter_type):
        self.type = parameter_type
    #Typisierung der Platte -> standard, black(Gulag), checkpoint, debris, ramp

    def __str__(self):
        return "Tile at " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "."

    def __repr__(self):
        return "Tile at " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "."

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def get_top(self):
        return self.top

    def get_right(self):
        return self.right

    def get_bot(self):
        return self.bot

    def get_left(self):
        return self.left

    def set_top(self, parameter):
        self.top = parameter

    def set_right(self, parameter):
        self.right = parameter

    def set_bot(self, parameter):
        self.bot = parameter

    def set_left(self, parameter):
        self.left = parameter
