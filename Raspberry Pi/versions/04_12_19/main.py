#MAZE 2020 MAIN

#IMPORTS
import map as map_lib
import maze_serial as m_ser
import tile
import wall
import arduinodata
import history
import stack
import custom_print
import logic
import sys
import data_storage

#SETUP

custom_print.start()

print("**********")
print("Log file opened")
print("**********")

m_ser.start()
print("Started serial communication")

map = map_lib.Map()
map.set_room(0, 0, 0)
current_x = 0
current_y = 0
current_z = 0

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

    # todo here comes logic module

    try:
        task_to_do = tasks.get()
        print("Took task from stack: ")
        print(task_to_do)
    except IndexError:
        print("Failed to take task from stack")
        print("Ending log")
        custom_print.stop()
        sys.exit()

    # todo here comes path module

    # todo send these instructions to arduino
    # todo start taking photos with around 5 frames per second
        # todo interrupt if victim and if not rescued yet
    # todo wait for arrival message
    # todo stop taking photos
    # todo update wanted rotation
    # todo update direction
    # todo update last driven in history module
    history.add_tile(current_tile)
    print("Updated last tile in history module: ")
    print(history.get_last_tile())
    # todo update current_tile
