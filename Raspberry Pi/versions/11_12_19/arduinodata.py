#maze 2020 arduinodata library
import data_storage
import custom_print
print = custom_print.update_print()
custom_print.start('arduinodata')


def decode(serial_string):
    print('Arduinodata decode function started')
    decoded_string = serial_string
    print('Decoded string:')
    print(decoded_string)
    decoded_string = serial_string.replace('\n', '')
    print('Decoded string without newline character:')
    print(decoded_string)
    decoded_string = decoded_string.replace('{', '')
    print('Decoded string without {:')
    print(decoded_string)
    decoded_string = decoded_string.replace('}', '')
    print('Decoded string without }:')
    print(decoded_string)
    decoded_string = decoded_string.replace(' ', '')
    print('Decoded string without spaces:')
    print(decoded_string)
    decoded_string = decoded_string.replace('"', '')
    print('Decoded string without double quotation marks:')
    print(decoded_string)
    decoded_string = decoded_string.replace('\'', '')
    print('Decoded string without quotation marks:')
    print(decoded_string)
    decoded_string = decoded_string.replace('[', '')
    print('Decoded string without [:')
    print(decoded_string)
    decoded_string = decoded_string.replace(']', '')
    print('Decoded string without ne]:')
    print(decoded_string)
    decoded_string = decoded_string.replace(':', ',')
    print('Decoded string without colons:')
    print(decoded_string)

    decoded_list = decoded_string.split(',')
    print('Decoded string split on commas:')
    print(decoded_string)

    decoded_dictionary = {}
    instance = None
    second_instance = 0
    position = None

    for item in range(len(decoded_list)):
        print('New cycle')
        if decoded_list[item] == 'temp':
            print('Found temp')
            decoded_dictionary['temp'] = {}
            instance = 'temp'
            continue

        if decoded_list[item] == 'ir':
            print('Found infrared')
            decoded_dictionary['ir'] = {}
            instance = 'ir'
            continue

        if decoded_list[item] == 'gyro':
            print('Found gyro')
            decoded_dictionary['gyro'] = {}
            instance = 'gyro'
            continue

        if decoded_list[item] == 'grayscale':
            print('Found grayscale')
            decoded_dictionary['grayscale'] = {}
            instance = 'grayscale'
            continue

        if decoded_list[item] == 'encoder':
            print('Found encoder')
            decoded_dictionary['encoder'] = {}
            instance = 'encoder'
            continue

        if instance == 'temp':
            print('In instance temp')
            if second_instance == 0:
                print('At sub instance 0')
                position = 'left_back'
                print(position)
                second_instance += 1
            elif second_instance == 1:
                print('At sub instance 1')
                position = 'left_front'
                print(position)
                second_instance += 1
            elif second_instance == 2:
                print('At sub instance 2')
                position = 'right_front'
                print(position)
                second_instance += 1
            elif second_instance == 3:
                print('At sub instance 3')
                position = 'right_back'
                print(position)
                second_instance = 0
            decoded_dictionary['temp'][position] = float(decoded_list[item])
            print('Decoded dictionary looks like this:')
            print(decoded_dictionary)
            continue

        if instance == 'ir':
            print('In instance temp')
            if second_instance == 0:
                print('At sub instance 0')
                position = 'left_back'
                print(position)
                second_instance += 1
            elif second_instance == 1:
                print('At sub instance 1')
                position = 'left_front'
                print(position)
                second_instance += 1
            elif second_instance == 2:
                print('At sub instance 2')
                position = 'front_left'
                print(position)
                second_instance += 1
            elif second_instance == 3:
                print('At sub instance 3')
                position = 'front_right'
                print(position)
                second_instance += 1
            elif second_instance == 4:
                print('At sub instance 4')
                position = 'right_front'
                print(position)
                second_instance += 1
            elif second_instance == 5:
                print('At sub instance 5')
                position = 'right_back'
                print(position)
                second_instance = 0
            decoded_dictionary['ir'][position] = float(decoded_list[item])
            print('Decoded dictionary looks like this:')
            print(decoded_dictionary)
            continue

        if instance == 'gyro':
            print('In instance gyro')
            if second_instance == 0:
                print('At sub instance 0')
                position = 'tilt'
                print(position)
                second_instance += 1
            elif second_instance == 1:
                print('At sub instance 1')
                position = 'rotation'
                print(position)
                second_instance = 0
            decoded_dictionary['gyro'][position] = float(decoded_list[item])
            print('Decoded dictionary looks like this:')
            print(decoded_dictionary)
            continue

        if instance == 'grayscale':
            print('In instance grayscale')
            if second_instance == 0:
                print('At sub instance 0')
                position = 'grayscale'
                print(position)
                second_instance = 0
            decoded_dictionary['grayscale'][position] = float(decoded_list[item])
            print('Decoded dictionary looks like this:')
            print(decoded_dictionary)
            continue

        if instance == 'encoder':
            print('In instance encoder')
            if second_instance == 0:
                print('At sub instance 0')
                position = 'left_back'
                print(position)
                second_instance += 1
            elif second_instance == 1:
                print('At sub instance 1')
                position = 'left_front'
                print(position)
                second_instance += 1
            elif second_instance == 2:
                print('At sub instance 2')
                position = 'right_front'
                print(position)
                second_instance += 1
            elif second_instance == 3:
                print('At sub instance 3')
                position = 'right_back'
                print(position)
                second_instance = 0
            decoded_dictionary['encoder'][position] = float(decoded_list[item])
            print('Decoded dictionary looks like this:')
            print(decoded_dictionary)
            continue

    print('Decoding completed')
    print(decoded_dictionary)
    return decoded_dictionary


def analyze(data, which_type):
    print('Arduinodata analyze function started')
    if which_type == 'all':
        print('Type is all')
        threshold = 10
        walls = {}

        print('Infrared value left_back is:')
        print(data['ir']['left_back'])
        print('Infrared value left_front is:')
        print(data['ir']['left_front'])
        if data['ir']['left_back'] <= threshold and data['ir']['left_front'] <= threshold:
            print('There is a freaking WALL on the left!')
            walls['left'] = 1
        else:
            print('There is no wall on the left!')
            walls['left'] = 0

        print('Infrared value front_left is:')
        print(data['ir']['front_left'])
        print('Infrared value front_right is:')
        print(data['ir']['front_right'])
        if data['ir']['front_left'] <= threshold and data['ir']['front_right'] <= threshold:
            print('There is a freaking WALL in the front')
            walls['front'] = 1
        else:
            print('There is no wall in the front!')
            walls['front'] = 0

        print('Infrared value right_front is:')
        print(data['ir']['right_front'])
        print('Infrared value right_back is:')
        print(data['ir']['right_back'])
        if data['ir']['right_front'] <= threshold and data['ir']['right_back'] <= threshold:
            print('There is a freaking WALL on the right!')
            walls['right'] = 1
        else:
            print('There is no wall on the right!')
            walls['right'] = 0
        walls['back'] = 0
        print('There is no wall in the back because that is where we are from!')

        print('Getting direction out of data_storage module')
        direction = data_storage.get_direction()
        print(direction)

        print('Calculating walls for the new direction')
        if direction == 0:
            print('Direction is already correct!')
            pass
        elif direction == 1:
            print('Turn everything by 90 degrees')
            temp_walls = walls
            walls['front'] = temp_walls['left']
            walls['right'] = temp_walls['front']
            walls['back'] = temp_walls['right']
            walls['left'] = temp_walls['back']
            print(walls)
        elif direction == 2:
            print('Turn everything by 180 degrees')
            temp_walls = walls
            walls['front'] = temp_walls['back']
            walls['right'] = temp_walls['left']
            walls['back'] = temp_walls['front']
            walls['left'] = temp_walls['right']
            print(walls)
        elif direction == 3:
            print('Turn everything by 270 degrees')
            temp_walls = walls
            walls['front'] = temp_walls['right']
            walls['right'] = temp_walls['back']
            walls['back'] = temp_walls['left']
            walls['left'] = temp_walls['front']
            print(walls)

        temp_border = 25
        victims = {}
        if data['temp']['left_back'] >= temp_border and data['temp']['left_front'] >= temp_border:
            victims['type'] = 'heat'
            victims['direction'] = 'left'
            victims['specs'] = None

        elif data['temp']['right_front'] >= temp_border and data['temp']['right_back'] >= temp_border:
            victims['type'] = 'heat'
            victims['direction'] = 'right'
            victims['specs'] = None

        else:
            victims['type'] = None
            victims['direction'] = None
            victims['specs'] = None

        grayscale_border = 25
        checkpoint_border = 75
        tilt_border = 10
        environment = {}
        if data['grayscale']['grayscale'] >= checkpoint_border:
            environment['floor'] = 'black'
        elif not data['grayscale']['grayscale'] > checkpoint_border and data['grayscale']['grayscale'] >= grayscale_border:
            environment['floor'] = 'checkpoint'
        else:
            environment['floor'] = 'checkpoint'

        if data['gyro']['tilt'] >= tilt_border:
            environment['tilt'] = 'ramp_up'
        elif data['gyro']['tilt'] <= (tilt_border * -1):
            environment['tilt'] = 'ramp_down'
        else:
            environment['tilt'] = 'straight'

        environment['rotation'] = data['gyro']['rotation']

        return walls, victims, environment, data['encoder']

    elif which_type == 'walls':
        threshold = 10
        walls = {}
        if data['ir']['left_back'] <= threshold and data['ir']['left_front'] <= threshold:
            walls['left'] = 1
        else:
            walls['left'] = 0

        if data['ir']['front_left'] <= threshold and data['ir']['front_left'] <= threshold:
            walls['front'] = 1
        else:
            walls['front'] = 0

        if data['ir']['right_front'] <= threshold and data['ir']['right_back'] <= threshold:
            walls['right'] = 1
        else:
            walls['right'] = 0
        walls['back'] = 0

        direction = data_storage.get_direction()
        if direction == 0:
            pass
        elif direction == 1:
            temp_walls = walls
            walls['front'] = temp_walls['left']
            walls['right'] = temp_walls['front']
            walls['back'] = temp_walls['right']
            walls['left'] = temp_walls['back']
        elif direction == 2:
            temp_walls = walls
            walls['front'] = temp_walls['back']
            walls['right'] = temp_walls['left']
            walls['back'] = temp_walls['front']
            walls['left'] = temp_walls['right']
        elif direction == 3:
            temp_walls = walls
            walls['front'] = temp_walls['right']
            walls['right'] = temp_walls['back']
            walls['back'] = temp_walls['left']
            walls['left'] = temp_walls['front']

        return walls

    elif which_type == 'victims':
        temp_border = 25
        victims = {}
        if data['temp']['left_back'] >= temp_border and data['temp']['left_front'] >= temp_border:
            victims['type'] = 'heat'
            victims['direction'] = 'left'
            victims['specs'] = None

        elif data['temp']['right_front'] >= temp_border and data['temp']['right_back'] >= temp_border:
            victims['type'] = 'heat'
            victims['direction'] = 'right'
            victims['specs'] = None

        else:
            victims['type'] = None
            victims['direction'] = None
            victims['specs'] = None

        return victims

    elif which_type == 'environment':
        grayscale_border = 75
        tilt_border = 10
        environment = {}
        if data['grayscale']['grayscale'] >= grayscale_border:
            environment['floor'] = 'black'
        else:
            environment['floor'] = 'white'

        if data['gyro']['tilt'] >= tilt_border:
            environment['tilt'] = 'ramp_up'
        elif data['gyro']['tilt'] <= (tilt_border * -1):
            environment['tilt'] = 'ramp_down'
        else:
            environment['tilt'] = 'straight'

        environment['rotation'] = data['gyro']['rotation']

        return environment

    elif which_type == 'motors':
        return data['encoder']
