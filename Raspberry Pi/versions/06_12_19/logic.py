#maze 2020 logic module

import data_storage
import stack
import tile
import map
import maze_serial as m_ser


def calculate_last_drive(coords):
    direction = data_storage.get_direction()
    if direction == 0:
        last_drive = [coords[0], coords[1] - 1, coords[2]]
    elif direction == 1:
        last_drive = [coords[0] - 1, coords[1], coords[2]]
    elif direction == 2:
        last_drive = [coords[0], coords[1] + 1, coords[2]]
    elif direction == 3:
        last_drive = [coords[0] + 1, coords[1], coords[2]]
    return last_drive


def run(map, tasks, wallsdata, victimsdata, environmentdata, motorsdata, coords):
    status = 0
    while status == 0:
        status = 1

        wanted_rotation = data_storage.get_wanted_rotation()
        actual_rotation = environmentdata['rotation']
        threshold = 25

        if wanted_rotation > actual_rotation:
            difference = abs(wanted_rotation) - abs(actual_rotation)
            if difference <= threshold:
                m_ser.send(('adjust' + str(difference) + '#'))
                answer = m_ser.receive()
                if answer == 'adjusted':
                    status = 0
                    continue
            elif difference > threshold:
                # todo enter PANIC MODE
                pass
        elif wanted_rotation < actual_rotation:
            difference = abs(actual_rotation) - abs(wanted_rotation)
            if difference <= threshold:
                m_ser.send(('adjust' + str(difference * -1) + '#'))
                answer = m_ser.receive()
                if answer == 'adjusted':
                    status = 0
                    continue
            elif difference > threshold:
                # todo enter PANIC MODE
                pass

        floor = environmentdata['floor']
        if floor == 'black':
            current_room = map.get_room(coords)
            current_room.set_type('black')
            map.set_room(coords, current_room)
            tasks.add(calculate_last_drive(coords))
            continue

        ramp_status = environmentdata['tilt']
        if ramp_status == 'ramp_up':
            tasks.add('ramp_up')
            continue

        current_room = map.get_room(coords)

        coords_left = coords
        coords_left[0] -= 1
        room_left = map.get_room(coords_left)
        if room_left == 0:
            if current_room.get_left == 'unknown':
                wall_left = environmentdata['left']
                if wall_left == 0:
                    map.add_room(coords_left)
                    tasks.add(coords)
                    current_room.set_left('open')
                    map.set_room(coords, current_room)
                elif wall_left == 1:
                    current_room.set_left('wall')
                    map.set_room(coords, current_room)

        coords_bot = coords
        coords_bot[1] -= 1
        room_bot = map.get_room(coords_bot)
        if room_bot == 0:
            if current_room.get_bot == 'unknown':
                wall_bot = environmentdata['back']
                if wall_bot == 0:
                    map.add_room(coords_bot)
                    tasks.add(coords)
                    current_room.set_bot('open')
                    map.set_room(coords, current_room)
                elif wall_bot == 1:
                    current_room.set_bot('wall')
                    map.set_room(coords, current_room)

        coords_right = coords
        coords_right[0] += 1
        room_right = map.get_room(coords_right)
        if room_right == 0:
            if current_room.get_right == 'unknown':
                wall_right = environmentdata['right']
                if wall_right == 0:
                    map.add_room(coords_right)
                    tasks.add(coords)
                    current_room.set_right('open')
                    map.set_room(coords, current_room)
                elif wall_right == 1:
                    current_room.set_right('wall')
                    map.set_room(coords, current_room)

        coords_top = coords
        coords_top[1] += 1
        room_top = map.get_room(coords_top)
        if room_top == 0:
            if current_room.get_top == 'unknown':
                wall_top = environmentdata['front']
                if wall_top == 0:
                    map.add_room(coords_top)
                    tasks.add(coords)
                    current_room.set_top('open')
                    map.set_room(coords, current_room)
                elif wall_top == 1:
                    current_room.set_top('wall')
                    map.set_room(coords, current_room)

# todo check for victims
    # todo update on map
    # todo calculate amount of rescue kits
    # todo dispense rescue kits

        floor = environmentdata['floor']
        if floor == 'checkpoint':
            data_storage.set_last_checkpoint_x(coords[0])
            data_storage.set_last_checkpoint_y(coords[1])
            data_storage.set_last_checkpoint_z(coords[2])

    return map, tasks


def update_direction(rotation):
    direction = data_storage.get_direction()
    if rotation == 90:
        direction += 1
    elif rotation == 180:
        direction += 2
    elif rotation == -90:
        direction -= 1

    if direction > 4:
        direction -= 4
    elif direction < 0:
        direction += 4

    data_storage.set_direction(direction)


def update_wanted_rotation(rotation):
    wanted_rotation = data_storage.get_wanted_rotation()
    wanted_rotation += rotation
    if wanted_rotation >= 360:
        wanted_rotation -= 360
    data_storage.set_wanted_rotation(wanted_rotation)


def update_coords(coords):
    direction = data_storage.get_direction()
    new_coords = None
    if direction == 0:
        new_coords = [coords[0], coords[1] + 1, coords[2]]
    elif direction == 1:
        new_coords = [coords[0] + 1, coords[1], coords[2]]
    elif direction == 2:
        new_coords = [coords[0], coords[1] - 1, coords[2]]
    elif direction == 3:
        new_coords = [coords[0] - 1, coords[1], coords[2]]

    return new_coords
