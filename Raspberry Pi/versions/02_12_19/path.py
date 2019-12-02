#maze 2020 path module
import waypoint

def next_path(current_tile, task_to_do):
    list_of_paths = list()
    node = waypoint.Waypoint(current_tile)
    current_tile.set_node(node)
    start_node = current_tile.get_node()
    current_path = list()
    all_paths = list()

    if current_tile.get_coordiantes()[0] > task_to_do.get_coordinates()[0]:
        prio_x = task_to_do.get_coordinates()[0] - current_tile.get_coordiantes()[0]
    elif current_tile.get_coordiantes()[0] < task_to_do.get_coordinates()[0]:
        prio_x = current_tile.get_coordiantes()[0] - task_to_do.get_coordinates()[0]
    else: #current_tile.get_coordiantes()[0] == task_to_do.get_coordinates()[0]:
        prio_x = 0

    if current_tile.get_coordiantes()[1] > task_to_do.get_coordinates()[1]:
        prio_y = task_to_do.get_coordinates()[1] - current_tile.get_coordiantes()[1]
    elif current_tile.get_coordiantes()[1] < task_to_do.get_coordinates()[1]:
        prio_y = current_tile.get_coordiantes()[1] - task_to_do.get_coordinates()[1]
    else: #current_tile.get_coordiantes()[1] == task_to_do.get_coordinates()[1]:
        prio_y = 0

    if current_tile.get_coordiantes()[2] > task_to_do.get_coordinates()[2]:
        prio_z = task_to_do.get_coordinates()[2] - current_tile.get_coordiantes()[2]
    elif current_tile.get_coordiantes()[2] < task_to_do.get_coordinates()[2]:
        prio_z = current_tile.get_coordiantes()[2] - task_to_do.get_coordinates()[2]
    else: #current_tile.get_coordiantes()[2] == task_to_do.get_coordinates()[2]:
        prio_z = 0

        # todo try ideal path
    if abs(prio_y) > abs(prio_x):
        if prio_y > 0:
            if prio_x > 0:
                # top is prio 1
                # right is prio 2
                while start_node is not None:
                    if 'top' in current_tile.get_node.get_pointer:
                        #top is möglich
                        current_tile = current_tile.get_top()
                        current_path.append('top')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_bot()
                            current_tile.get_node.remove('top')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_bot()
                            current_tile.get_node.remove('top')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
                    elif 'right' in current_tile.get_node.get_pointer:
                    # top is nicht möglich aber right dafür
                        current_tile = current_tile.get_rgt()
                        current_path.append('right')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_lft()
                            current_tile.get_node.remove('right')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_lft()
                            current_tile.get_node.remove('right')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
            elif prio_x < 0:
                # top is prio 1
                # left is prio 2
                while start_node is not None:
                    if 'top' in current_tile.get_node.get_pointer:
                        #top is möglich
                        current_tile = current_tile.get_top()
                        current_path.append('top')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_bot()
                            current_tile.get_node.remove('top')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_bot()
                            current_tile.get_node.remove('top')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
                    elif 'left' in current_tile.get_node.get_pointer:
                    # top is nicht möglich aber left dafür
                        current_tile = current_tile.get_lft()
                        current_path.append('left')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_rgt()
                            current_tile.get_node.remove('left')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_rgt()
                            current_tile.get_node.remove('left')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
            elif prio_x == 0:
                # top is prio 1 (and only prio)
                while start_node is not None:
                    if 'top' in current_tile.get_node.get_pointer:
                        # top is möglich
                        current_tile = current_tile.get_top()
                        current_path.append('top')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_bot()
                            current_tile.get_node.remove('top')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_bot()
                            current_tile.get_node.remove('top')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
        elif prio_y < 0:
            if prio_x > 0:
                # bot is prio 1
                # right is prio 2
                while start_node is not None:
                    if 'bot' in current_tile.get_node.get_pointer:
                        #bot is möglich
                        current_tile = current_tile.get_bot()
                        current_path.append('bot')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_top()
                            current_tile.get_node.remove('bot')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_top()
                            current_tile.get_node.remove('bot')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
                    elif 'right' in current_tile.get_node.get_pointer:
                    # top is nicht möglich aber right dafür
                        current_tile = current_tile.get_lft()
                        current_path.append('right')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_lft()
                            current_tile.get_node.remove('right')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_lft()
                            current_tile.get_node.remove('right')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
            elif prio_x < 0:
                # bot is prio 1
                # left is prio 2
                while start_node is not None:
                    if 'bot' in current_tile.get_node.get_pointer:
                        #bot is möglich
                        current_tile = current_tile.get_bot()
                        current_path.append('bot')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_top()
                            current_tile.get_node.remove('bot')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_top()
                            current_tile.get_node.remove('bot')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
                    elif 'left' in current_tile.get_node.get_pointer:
                    # top is nicht möglich aber left dafür
                        current_tile = current_tile.get_rgt()
                        current_path.append('left')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_rgt()
                            current_tile.get_node.remove('left')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_rgt()
                            current_tile.get_node.remove('left')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
            elif prio_x == 0:
                #bot is prio 1 (and only prio)
                while start_node is not None:
                    if 'bot' in current_tile.get_node.get_pointer:
                        #bot is möglich
                        current_tile = current_tile.get_bot()
                        current_path.append('bot')
                        if current_tile.get_node is None:
                            current_tile = current_tile.get_top()
                            current_tile.get_node.remove('bot')
                            current_path.pop()
                            continue
                        elif current_tile is task_to_do:
                            all_paths.append(current_path)
                            current_tile = current_tile.get_top()
                            current_tile.get_node.remove('bot')
                            current_path.pop()
                            continue
                        else:
                            node = waypoint.Waypoint(current_tile)
                            continue
    elif abs(prio_x) > abs(prio_y):
        if prio_x > 0:
            if prio_y > 0:
                #right is prio 1
                # top is prio 2
            elif prio_y < 0:
                #right is prio 1
                # bot is prio 2
            elif prio_y == 0:
                #right is prio 1 (and only prio)
        elif prio_x < 0:
            if prio_y > 0:
                #left is prio 1
                # top is prio 2
            elif prio_y < 0:
                #left is prio 1
                # bot is prio 2
            elif prio_y == 0:
                #left is prio 1 (and only prio)


    # todo find best
    # todo return best path
