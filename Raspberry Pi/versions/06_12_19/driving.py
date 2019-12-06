#maze 2020 driving module
import data_storage


def by_path(path, coords):
    first_room = path[0]
    rotation = data_storage.get_rotation()
    instructions = list()

    if first_room[1] > coords[1]:
        if rotation != 0:
            if rotation == 1:
                instructions.append(['turn', '-90'])
            elif rotation == 2:
                instructions.append(['turn', '180'])
            elif rotation == 3:
                instructions.append(['turn', '90'])
    elif first_room[0] > coords[0]:
        if rotation != 1:
            if rotation == 0:
                instructions.append(['turn', '90'])
            elif rotation == 2:
                instructions.append(['turn', '-90'])
            elif rotation == 3:
                instructions.append(['turn', '180'])
    elif first_room[1] < coords[1]:
        if rotation != 2:
            if rotation == 0:
                instructions.append(['turn', '180'])
            elif rotation == 1:
                instructions.append(['turn', '90'])
            elif rotation == 3:
                instructions.append(['turn', '-90'])
    elif first_room[0] < coords[0]:
        if rotation != 3:
            if rotation == 0:
                instructions.append(['turn', '-90'])
            elif rotation == 1:
                instructions.append(['turn', '180'])
            elif rotation == 2:
                instructions.append(['turn', '90'])

    instructions.append(['straight', ''])

    return instructions
