#Maze 2020 history module

prev_driven = []
prev_tile = []


def add_driven(new):
    prev_driven.append(new)


def add_tile(new):
    prev_tile.append(new)


def get_last_drive():
    return prev_driven[-1]


def get_last_tile():
    return prev_tile[-1]
