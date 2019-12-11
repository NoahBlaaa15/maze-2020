#MAZE 2020 MAIN

# todo 2 external pi's with the cams, sending interrupts when image
# todo install camera interrupts
# todo install lack of progress interrupts
# todo add a lot of logs

#IMPORTS
import map as map_lib
import maze_serial as m_ser
import arduinodata
import stack
import custom_print
import logic
import sys
import path
import driving

#SETUP

print = custom_print.update_print()
custom_print.start('main')

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

    map, tasks = logic.run(map, tasks, wallsdata, victimsdata, environmentdata, motorsdata, coords)

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
    change_rotation = 0
    if next_path != 'ramp_up' and next_path != 'ramp_down':
        drive_instructions = driving.by_path(next_path, coords)
        for i in range(len(drive_instructions)):
            m_ser.send((drive_instructions[i][0] + drive_instructions[i][1] + '#'))
            answer = m_ser.receive()
            if answer != drive_instructions[i][0] + 'ed':
                # todo FUCK FUCK FUCK
                pass
            if drive_instructions[i][0] == 'turn':
                change_rotation = int(drive_instructions[i][1])
    else:
        m_ser.send((next_path + '#'))
        answer = m_ser.receive()

    logic.update_wanted_rotation(change_rotation)
    logic.update_direction(change_rotation)
    coords = logic.update_coords(coords)
    logic.update_last_driven()
