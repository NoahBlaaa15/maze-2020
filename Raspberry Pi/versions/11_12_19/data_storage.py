#maze 2020 data storage module
import custom_print
print = custom_print.update_print()
direction = 0
wanted_rotation = 0
tile_counter = 0
last_checkpoint_x = 0
last_checkpoint_y = 0
last_checkpoint_z = 0


def get_direction():
    print("data_storage get_direction function called")
    global direction
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'direction = '
    index = content.find(here)
    direction = int(content[index+len(here)])
    print("Direction is: ", direction, ". About to return.")
    return direction


def set_direction(new_direction):
    print("data_storage set_direction function called")
    global direction
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'direction = '
    new_string = here + str(new_direction)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    print("Setting direction ", direction, " to ", new_direction, ".")
    direction = new_direction


def get_wanted_rotation():
    print("data_storage get_wanted_rotation function called")
    global wanted_rotation
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'wanted_rotation = '
    index = content.find(here)
    wanted_rotation = int(content[index + len(here)])
    print("Wanted rotation is: ", wanted_rotation, ". About to return.")
    return wanted_rotation


def set_wanted_rotation(new_wanted_rotation):
    print("data_storage set_wanted_rotation function called")
    global wanted_rotation
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'wanted_rotation = '
    new_string = here + str(new_wanted_rotation)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    print("Setting wanted rotation ", wanted_rotation, " to ", new_wanted_rotation, ".")
    wanted_rotation = new_wanted_rotation


def get_last_checkpoint_x():
    print("data_storage get_last_checkpoint_x function called")
    global last_checkpoint_x
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_x = '
    index = content.find(here)
    last_checkpoint_x = int(content[index + len(here)])
    print("Last checkpoint x is: ", last_checkpoint_x, ". About to return.")
    return last_checkpoint_x


def set_last_checkpoint_x(new_last_checkpoint_x):
    print("data_storage set_last_checkpoint_x function called")
    global last_checkpoint_x
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_x = '
    new_string = here + str(new_last_checkpoint_x)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    print("Setting last checkpoint x ", last_checkpoint_x, " to ", new_last_checkpoint_x, ".")
    last_checkpoint_x = new_last_checkpoint_x


def get_last_checkpoint_y():
    print("data_storage get_last_checkpoint_y function called")
    global last_checkpoint_y
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_y = '
    index = content.find(here)
    last_checkpoint_y = int(content[index + len(here)])
    print("Last checkpoint y is: ", last_checkpoint_y, ". About to return.")
    return last_checkpoint_y


def set_last_checkpoint_y(new_last_checkpoint_y):
    print("data_storage set_last_checkpoint_y function called")
    global last_checkpoint_y
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_y = '
    new_string = here + str(new_last_checkpoint_y)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    print("Setting last checkpoint y ", last_checkpoint_y, " to ", new_last_checkpoint_y, ".")
    last_checkpoint_y = new_last_checkpoint_y


def get_last_checkpoint_z():
    print("data_storage get_last_checkpoint_z function called")
    global last_checkpoint_z
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_z = '
    index = content.find(here)
    last_checkpoint_z = int(content[index + len(here)])
    print("Last checkpoint z is: ", last_checkpoint_z, ". About to return.")
    return last_checkpoint_z


def set_last_checkpoint_z(new_last_checkpoint_z):
    print("data_storage set_last_checkpoint_z function called")
    global last_checkpoint_z
    with open('data.txt', 'r') as content_file:
        content = content_file.read()
    here = 'last_checkpoint_z = '
    new_string = here + str(new_last_checkpoint_z)
    index = content.find(here)
    new_content = content[:index] + new_string + content[index+len(new_string):]
    with open('data.txt', 'w') as content_file:
        content_file.write(new_content)
    print("Setting last checkpoint z ", last_checkpoint_z, " to ", new_last_checkpoint_z, ".")
    last_checkpoint_z = new_last_checkpoint_z
