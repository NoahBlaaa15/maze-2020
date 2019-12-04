#maze 2020 map module
import numpy as np
import tile


class Map:

    def __init__(self):
        self.map = np.zeros(31, 31, 3)

    def get_room(self, x, y, z):
        return self.map[x + 15][y + 15][z + 1]

    def set_room(self, x, y, z):
        adj_x = x + 15
        adj_y = y + 15
        adj_z = z + 1
        self.map[adj_x][adj_y][adj_z] = tile.Tile(adj_x, adj_y, adj_z)

    def __str__(self):
        return "The official map object for holding all the rooms/tiles!"

    def __repr__(self):
        return "The official map object for holding all the rooms/tiles!"
