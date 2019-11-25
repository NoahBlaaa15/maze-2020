#maze 2020 logic module

#Setup
import data_storage
import tile

glob_wallsdata = None
glob_victimsdata = None
glob_environmentdata = None
glob_motorsdata = None
current_tile = None
tasks = None
status = 0
direction = data_storage.get_direction()
wanted_direction = data_storage.get_wanted_direction()

#Modules

def check_rotation(environmentdata, motorsdata):
    global status
    threshold = 15
    if environmentdata['rotation'] <= data_storage.get_wanted_rotation() - threshold:
        tasks.add('Adjust more')
        pass
    elif environmentdata['rotation'] >= data_storage.get_wanted_rotation() + threshold:
        tasks.add('Adjust less')
        pass
    status = 1

def black_tile(environmentdata):
    global tasks
    global current_tile
    global status
    if environmentdata['floor'] == 'black':
        print("Black tile")
        current_tile.set_type('black')
        print("Changed type")
        current_tile.set_top(wall.Wall())
        print("Top locked")
        current_tile.set_rgt(wall.Wall())
        print("Right locked")
        current_tile.set_but(wall.Wall())
        print("Down locked")
        current_tile.set_lft(wall.Wall())
        print("Left locked")

        tasks.add(history.get_last_tile())
        print("Added reverse to stack")
        print(tasks)
        print(tasks.all())
        status = 1

def ramp_check(environmentdata):
    if environmentdata['tilt'] == 'ramp_up':
        # todo perform ramp check
        tasks.add('Ramp up')
        status = 1
    elif environmentdata['tilt'] == 'ramp_down':
        # todo perform ramp check
        tasks.add('Ramp down')
        status = 1

def map_update(wallsdata):
    global current_tile
    global direction
    global tasks

    if direction == 0:
        pass
    elif direction == 1:
        temp_wallsdata = wallsdata
        wallsdata['front'] = temp_wallsdata['left']
        wallsdata['right'] = temp_wallsdata['front']
        wallsdata['back'] = temp_wallsdata['right']
        wallsdata['left'] = temp_wallsdata['back']
    elif direction == 2:
        temp_wallsdata = wallsdata
        wallsdata['front'] = temp_wallsdata['back']
        wallsdata['right'] = temp_wallsdata['left']
        wallsdata['back'] = temp_wallsdata['front']
        wallsdata['left'] = temp_wallsdata['right']
    elif direction == 3:
        temp_wallsdata = wallsdata
        wallsdata['front'] = temp_wallsdata['right']
        wallsdata['right'] = temp_wallsdata['back']
        wallsdata['back'] = temp_wallsdata['left']
        wallsdata['left'] = temp_wallsdata['front']


    if current_tile.has_lft() == False:
        if wallsdata['left'] == 0:
            tile = tile.Tile()
            current_tile.set_lft(tile)
            tasks.add(tile)
        else:
            wall = wall.Wall()
            current_tile.set_lft(wall)

    if current_tile().has_bot() == False:
        if wallsdata['down'] == 0:
            tile = tile.Tile()
            current_tile.set_bot(tile)
            tasks.add(tile)
        else:
            wall = wall.Wall()
            current_tile.set_bot(wall)

    if current_tile.has_rgt() == False:
        if wallsdata['right'] == 0:
            tile = tile.Tile()
            current_tile.set_rgt(tile)
            tasks.add(tile)
        else:
            wall = wall.Wall()
            current_tile.set_rgt(wall)

    if current_tile.has_top() == False:
        if wallsdata['front'] == 0:
            tile = tile.Tile()
            current_tile.set_top(tile)
            tasks.add(tile)
        else:
            wall = wall.Wall()
            current_tile.set_top(wall)


def victims_check(victimsdata):
    # todo check for heat_victims
    # todo modify and check the walls based on this information
    # todo deploy kits if not yet rescued
    pass

def check_checkpoint(environmentdata):
    if environmentdata['floor'] == 'checkpoint':
        # todo change last visited checkpoint
        pass

def calculate_action(parameter_wallsdata, parameter_victimsdata, parameter_environmentdata, parameter_motorsdata, parameter_current_tile, parameter_tasks):
    global glob_wallsdata
    global glob_victimsdata
    global glob_environmentdata
    global glob_motorsdata
    global direction
    global status
    global wanted_direction

    glob_wallsdata = parameter_wallsdata
    glob_victimsdata = parameter_victimsdata
    glob_environmentdata = parameter_environmentdata
    glob_motorsdata = parameter_motorsdata
    current_tile = parameter_current_tile
    tasks = parameter_tasks
    status = 0
    direction = data_storage.get_direction()
    wanted_direction = data_storage.get_wanted_direction()

    if status == 0:
        check_rotation(glob_environmentdata, glob_motorsdata)
    if status == 0:
        black_tile(glob_environmentdata)
    if status == 0:
        ramp_check(glob_environmentdata)
    if status == 0:
        map_update(glob_wallsdata)
    if status == 0:
        victims_check(glob_victimsdata)
    if status == 0:
        check_checkpoint(glob_environmentdata)

    data_storage.set_direction(direction)

    return current_tile, tasks
