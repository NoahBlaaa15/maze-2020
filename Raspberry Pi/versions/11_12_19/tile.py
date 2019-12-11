#maze 2020 tile library
import data_storage

class Tile:

    def __init__(self, coords):
        #Those are integers
        self.coords = coords

        #Those are 'unknown', 'wall' or 'open'
        self.top = 'unknown'
        self.right = 'unknown'
        self.bot = 'unknown'
        self.left = 'unknown'

        self.cost = 0
        self.type = 'standard'
        self.visited = False

    def set_type(self, parameter_type):
        self.type = parameter_type
    #Typisierung der Platte -> standard, black(Gulag), checkpoint, debris, ramp, ramp_access

    def get_type(self):
        return self.type

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

    def calculate_cost(self, target_coords):
        if target_coords[0] > self.coords[0]:
            if target_coords[1] > self.coords[1]:
                # target is at right and top
                x_difference = target_coords[0] - self.coords[0]
                y_difference = target_coords[1] - self.coords[1]
                self.cost = x_difference + y_difference
            elif target_coords[1] < self.coords[1]:
                # target is at right and bot
                x_difference = target_coords[0] - self.coords[0]
                y_difference = self.coords[1] - target_coords[1]
                self.cost = x_difference + y_difference
            else:
                # target is at right
                x_difference = target_coords[0] - self.coords[0]
                self.cost = x_difference
        elif target_coords[0] < self.coords[0]:
            if target_coords[1] > self.coords[1]:
                # target is at left and top
                x_difference = self.coords[0] - target_coords[0]
                y_difference = target_coords[1] - self.coords[1]
                self.cost = x_difference + y_difference
            elif target_coords[1] < self.coords[1]:
                # target is at left and bot
                x_difference = self.coords[0] - target_coords[0]
                y_difference = self.coords[1] - target_coords[1]
                self.cost = x_difference + y_difference
            else:
                # target is at left
                x_difference = self.coords[0] - target_coords[0]
                self.cost = x_difference
        else:
            if target_coords[1] > self.coords[1]:
                # target is at top
                y_difference = target_coords[1] - self.coords[1]
                self.cost = y_difference
            elif target_coords[1] < self.coords[1]:
                # target is at bot
                y_difference = self.coords[1] - target_coords[1]
                self.cost = y_difference
            else:
                #target is here
                self.cost = 0

    def get_cost(self):
        return self.cost

    def get_any(self, which):
        if which == 'top':
            return self.top
        elif which == 'right':
            return self.right
        elif which == 'bot':
            return self.bot
        elif which == 'left':
            return self.left