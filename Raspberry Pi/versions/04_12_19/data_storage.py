#maze 2020 data storage module

direction = 0
wanted_rotation = 0
tile_counter = 0
last_checkpoint_x = 0
last_checkpoint_y = 0
last_checkpoint_z = 0


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


'''def get_tile_counter():
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
'''

def get_last_checkpoint_x():
    global last_checkpoint_x
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_x = '
    index = content.find(here)
    last_checkpoint_x = int(content[index + len(here)])
    return last_checkpoint_x


def set_last_checkpoint_x(new_last_checkpoint_x):
    global last_checkpoint_x
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_x = '
    new_string = here + str(new_last_checkpoint_x)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    last_checkpoint_x = new_last_checkpoint_x


def get_last_checkpoint_y():
    global last_checkpoint_y
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_y = '
    index = content.find(here)
    last_checkpoint_y = int(content[index + len(here)])
    return last_checkpoint_y


def set_last_checkpoint_y(new_last_checkpoint_y):
    global last_checkpoint_y
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_y = '
    new_string = here + str(new_last_checkpoint_y)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    last_checkpoint_y = new_last_checkpoint_y


def get_last_checkpoint_z():
    global last_checkpoint_z
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_z = '
    index = content.find(here)
    last_checkpoint_z = int(content[index + len(here)])
    return last_checkpoint_z


def set_last_checkpoint_z(new_last_checkpoint_z):
    global last_checkpoint_z
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_z = '
    new_string = here + str(new_last_checkpoint_z)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    last_checkpoint_z = new_last_checkpoint_z