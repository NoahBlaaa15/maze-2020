#maze 2020 path module


def by_cost(queue):
    return queue[2]


def calculate_path(task, map, coords):

    ramp_access_points = list()

    if task == 'ramp_up':
        return task
    elif task == 'ramp_down':
        return task

    for x in range(-15, 15):
        for y in range(-15, 15):
            temp_coords = [x, y, coords[2]]
            temp_room = map.get_room(temp_coords)
            temp_room.calculate_cost([task[0], task[1], coords[2]])
            map.set_room(temp_coords, temp_room)
            if temp_room.get_type() == 'ramp_access':
                temp_coords.append(temp_room.get_cost())
                ramp_access_points.append(temp_coords)

    if task[2] != coords[2]:
        if len(ramp_access_points) == 1:
            task = ramp_access_points[0]
        elif len(ramp_access_points) > 1:
            ramp_access_points.sort(key=lambda ramp_acces_points: ramp_acces_points[3])
            task = ramp_access_points[0][:3]

    queue = []
    done = []

    start = [coords, map.get_room(coords).get_cost(), 'start']
    current = start

    while current[0] != task:
        if map.get_room(current[0]).get_top() == 'open':
            coords_top = [current[0][0], current[0][1] + 1, current[0][2]]
            room_top = map.get_room(coords_top)
            top = [coords_top, room_top.get_cost(), current]
            if top not in queue:
                queue.append(top)
            else:
                alternative_top = None
                index_alternative_top = None
                for i in queue:
                    if coords_top in i:
                        alternative_top = i
                        index_alternative_top = queue.index(i)
                if alternative_top[2] > top[2]:
                    queue[index_alternative_top] = top

        if map.get_room(current[0]).get_right() == 'open':
            coords_right = [current[0][0] + 1, current[0][1], current[0][2]]
            room_right = map.get_room(coords_right)
            right = [coords_right, room_right.get_cost(), current]
            if right not in queue:
                queue.append(right)
            else:
                alternative_right = None
                index_alternative_right = None
                for i in queue:
                    if coords_right in i:
                        alternative_right = i
                        index_alternative_right = queue.index(i)
                if alternative_right[2] > right[2]:
                    queue[index_alternative_right] = right

        if map.get_room(current[0]).get_bot() == 'open':
            coords_bot = [current[0][0], current[0][1] - 1, current[0][2]]
            room_bot = map.get_room(coords_bot)
            bot = [coords_bot, room_bot.get_cost(), current]
            if bot not in queue:
                queue.append(bot)
            else:
                alternative_bot = None
                index_alternative_bot = None
                for i in queue:
                    if coords_bot in i:
                        alternative_bot = i
                        index_alternative_bot = queue.index(i)
                if alternative_bot[2] > bot[2]:
                    queue[index_alternative_bot] = bot

        if map.get_room(current[0]).get_left() == 'open':
            coords_left = [current[0][0] - 1, current[0][1], current[0][2]]
            room_left = map.get_room(coords_left)
            left = [coords_left, room_left.get_cost(), current]
            if left not in queue:
                queue.append(left)
            else:
                alternative_left = None
                index_alternative_left = None
                for i in queue:
                    if coords_left in i:
                        alternative_left = i
                        index_alternative_left = queue.index(i)
                if alternative_left[2] > left[2]:
                    queue[index_alternative_left] = left

        done.append(current)
        queue.sort(key=by_cost)
        current = queue[0]
        queue.pop(0)

    actual_path = list()
    while current[2] != 'start':
        actual_path.append(current[0])
        current = done[2]
    actual_path.reverse()

    #actual_path looks like this: [[x, y, z], [x, y, z], ...]
    return actual_path
