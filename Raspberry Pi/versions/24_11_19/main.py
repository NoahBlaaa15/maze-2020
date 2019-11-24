#MAZE 2020 MAIN

#IMPORTS
import maze_serial as m_ser
import tile
import wall
import arduinodata
import history
import stack
import custom_print

#SETUP

custom_print.start()

print("**********")
print("Log file opened")
print("**********")

m_ser.start()
print("Started serial communication")

tile = tile.Tile()
print("Created initial tile")

current_tile = tile
print("Moved room from tile to current_tile")

tasks = stack.Stack()
print("Initialised stack")

#ACTION
while True:
    m_ser.send('pls#')
    print("Requested data from Arduino")
    data = m_ser.receive()
    print("Received data from arduino")
    
    data = arduinodata.decode(data)
    print("Unzipped received data: ")
    print(data)
    wallsdata, victimsdata, environmentdata, motorsdata = arduinodata.analyze(data, 'all')
    print("Analysed unzipped data")
    for i in wallsdata:
        print(i, wallsdata[i])
    for i in victimsdata:
        print(i, victimsdata[i])
    for i in environmentdata:
        print(i, environmentdata[i])
    for i in motorsdata:
        print(i, motorsdata[i])
    # todo analyse camera data

    # todo check rotation values
        # todo if not correct send adjustment commands
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
        # todo goto driving section
        
    # todo check for ramp
        # todo enter ramp driving mode
    # todo check for undefined tiles around current tile
        # todo create missing tiles and set walls depending on the data received from arduino
        # todo check if there is a wall and if tile is already visited for new tiles
        # todo add visiting said tile to stack
    # todo check for victims
        # todo modify and check the walls based on this information
        # todo deploy kits if not yet rescued
    # todo check for checkpoint
        # todo change last visited tile
    
    try:
        task_to_do = tasks.get()
        print("Took task from stack: ")
        print(task_to_do)
    except IndexError:
        print("Failed to take task from stack")
        print("Ending log")
        custom_print.stop()
        # todo end run
    # todo decode task to exact instructions
    # todo send these instructions to arduino
    # todo start taking photos with around 15 frames per second
    # todo wait for arrival message
    # todo stop taking photos
    # todo start object detection
    # todo update last driven in history module
    history.add_tile(current_tile)
    print("Updated last tile in history module: ")
    print(history.get_last_tile())
    # todo update current_tile
