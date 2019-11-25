#maze 2020 data storage module

direction = 0
wanted_rotation = 0
tile_counter = 0

def get_direction():
    global direction
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'direction = '
    index = content.find(here)
    direction = int(content[index+len(here)])
    return direction

def set_direction(new_direction):
    global direction
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'direction = '
    new_string = here + str(new_direction)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    direction = new_direction

def get_wanted_rotation():
    global wanted_rotation
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'wanted_rotation = '
    index = content.find(here)
    wanted_rotation = int(content[index + len(here)])
    return wanted_rotation

def set_wanted_rotation(new_wanted_rotation):
    global wanted_rotation
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'wanted_rotation = '
    new_string = here + str(new_wanted_rotation)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    wanted_rotation = new_wanted_rotation

def get_tile_counter():
    global tile_counter
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'tile_counter = '
    index = content.find(here)
    tile_counter = int(content[index + len(here)])
    return tile_counter

def set_tile_counter(new_tile_counter):
    global tile_counter
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'tile_counter = '
    new_string = here + str(new_tile_counter)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    tile_counter = new_tile_counter

def add_tile_counter():
    global tile_counter
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'tile_counter = '
    new_string = here + str(tile_counter + 1)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    tile_counter +=1