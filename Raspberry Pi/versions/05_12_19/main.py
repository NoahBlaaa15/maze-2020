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
import path

#SETUP

custom_print.start()

print("**********")
print("Log file opened")
print("**********")

m_ser.start()
print("Started serial communication")

map = map_lib.Map()
coords = [0, 0, 0]
map.add_room(coords)

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

    map, tasks = logic.run(map, tasks, wallsdata, victimsdata, environmentdata, motorsdata, coords, history.get_last_drive)

    try:
        task_to_do = tasks.get()
        print("Took task from stack: ")
        print(task_to_do)
    except IndexError:
        if coords == [0, 0, 0]:
            print("Failed to take task from stack")
            print("Ending log")
            custom_print.stop()
            sys.exit()
        else:
            task_to_do = [0, 0, 0]

    next_path = path.calculate_path(task_to_do, map, coords)

    # todo calculate precise driving instruction from path
    # todo send these instructions to arduino
    # todo start taking photos with around 5 frames per second
        # todo interrupt if visual victim and if not rescued yet
    # todo wait for arrival message
    # todo stop taking photos
    # todo update wanted rotation
    # todo update direction
    # todo update last driven in history module
    history.add_tile(current_tile)
    print("Updated last tile in history module: ")
    print(history.get_last_tile())
    # todo update current_tile
