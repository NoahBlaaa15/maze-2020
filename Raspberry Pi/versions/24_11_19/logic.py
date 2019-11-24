#maze 2020 logic module

#Setup
glob_wallsdata = None
glob_victimsdata = None
glob_environmentdata = None
glob_motorsdata = None
current_tile = None
tasks = None
status = 0
direction = None

#Modules

def check_rotation(environmentdata, motorsdata):
    global status
    pass
    # todo check rotation values and motor encoders
    # todo if not correct send adjustment commands
    # todo change status if necessary

def black_tile(environmentdata):
    global tasks
    global current_tile
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
        # todo change status if necessary

def ramp_check(environmentdata):
    if environmentdata['tilt'] == 'ramp_up':
        # todo enter ramp driving mode
        # todo change status if necessary
        pass
    elif environmentdata['tilt'] == 'ramp_down':
        # todo enter ramp driving mode
        # todo change status if necessary
        pass

def map_update(wallsdata):
    global current_tile
    global direction

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
        # todo create missing tiles and set walls depending on the data received from arduino
        # todo check if there is a wall and if tile is already visited for new tiles
        # todo add visiting said tile to stack
        if wallsdata['left'] == 0:
            kachel
    if current_tile().has_bot() == False:
        # todo create missing tiles and set walls depending on the data received from arduino
        # todo check if there is a wall and if tile is already visited for new tiles
        # todo add visiting said tile to stack
        pass
    if current_tile.has_rgt() == False:
        # todo create missing tiles and set walls depending on the data received from arduino
        # todo check if there is a wall and if tile is already visited for new tiles
        # todo add visiting said tile to stack
        pass
    if current_tile.has_top() == False:
        # todo create missing tiles and set walls depending on the data received from arduino
        # todo check if there is a wall and if tile is already visited for new tiles
        # todo add visiting said tile to stack
        pass

def victims_check(victimsdata):
    # todo check for victims
    # todo modify and check the walls based on this information
    # todo deploy kits if not yet rescued
    pass

def check_checkpoint(environmentdata):
    # todo check for checkpoint
    # todo change last visited checkpoint
    pass

def calculate_action(parameter_wallsdata, parameter_victimsdata, parameter_environmentdata, parameter_motorsdata, parameter_current_tile, parameter_tasks, parameter_direction):
    global glob_wallsdata
    global glob_victimsdata
    global glob_environmentdata
    global glob_motorsdata
    global direction

    glob_wallsdata = parameter_wallsdata
    glob_victimsdata = parameter_victimsdata
    glob_environmentdata = parameter_environmentdata
    glob_motorsdata = parameter_motorsdata
    current_tile = parameter_current_tile
    tasks = parameter_tasks
    direction = parameter_direction

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

    return current_tile, tasks
