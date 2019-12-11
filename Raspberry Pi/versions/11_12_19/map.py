#maze 2020 map module
import numpy as np
import tile


class Map:

    def __init__(self):
        self.map = np.zeros([31, 31, 3])

    def get_room(self, coords):
        return self.map[coords[0] + 15][coords[1] + 15][coords[2] + 1]

    def add_room(self, coords):
        adj_x = coords[0] + 15
        adj_y = coords[1] + 15
        adj_z = coords[2] + 1
        self.map[adj_x][adj_y][adj_z] = tile.Tile(adj_x, adj_y, adj_z)

    def set_room(self, coords, room):
        adj_x = coords[0] + 15
        adj_y = coords[1] + 15
        adj_z = coords[2] + 1
        self.map[adj_x][adj_y][adj_z] = room

    def __str__(self):
        return "The official map object for holding all the rooms/tiles!"

    def __repr__(self):
        return "The official map object for holding all the rooms/tiles!"

    def get_top(self, coords):
        return  self.map[coords[0] + 15][coords[1] + 16][coords[2] + 1]

    def get_right(self, coords):
        return  self.map[coords[0] + 16][coords[1] + 15][coords[2] + 1]

    def get_bot(self, coords):
        return  self.map[coords[0] + 15][coords[1] + 14][coords[2] + 1]

    def get_left(self, coords):
        return  self.map[coords[0] + 14][coords[1] + 15][coords[2] + 1]
