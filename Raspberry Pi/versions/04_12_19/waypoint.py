#maze 2020 waypoint module
import tile

class Waypoint:
    def __init__(self, current_tile):
        self.pointer = list()
        self.coords = current_tile.get_coordinates()

        if current_tile.has_lft:
            if isinstance(current_tile.get_lft, tile.Tile):
                if current_tile.get_lft.get_visited:
                    self.pointer.append('lft')
        if current_tile.has_bot:
            if isinstance(current_tile.get_bot, tile.Tile):
                if current_tile.get_bot.get_visited:
                    self.pointer.append('bot')
        if current_tile.has_rgt:
            if isinstance(current_tile.get_rgt, tile.Tile):
                if current_tile.get_rgt.get_visited:
                    self.pointer.append('right')
        if current_tile.has_top:
            if isinstance(current_tile.get_top, tile.Tile):
                if current_tile.get_top.get_visited:
                    self.pointer.append('top')

    def __str__(self):
        return "Waypoint of Tile " + current_tile + "."

    def __repr__(self):
        return "Waypoint of Tile " + current_tile + "."

    def get_pointer(self):
        return self.pointer

    def remove(self, direction):
        if direction in self.pointer:
            self.pointer.remove(direction)
