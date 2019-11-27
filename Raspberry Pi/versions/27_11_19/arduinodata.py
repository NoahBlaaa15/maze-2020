#maze 2020 arduinodata library

def decode(serial_string):
    decoded_string = serial_string.replace('\n', '')
    decoded_string = decoded_string.replace('{', '')
    decoded_string = decoded_string.replace('}', '')
    decoded_string = decoded_string.replace(' ', '')
    decoded_string = decoded_string.replace('"', '')
    decoded_string = decoded_string.replace('\'', '')
    decoded_string = decoded_string.replace('[', '')
    decoded_string = decoded_string.replace(']', '')
    decoded_string = decoded_string.replace(':', ',')

    decoded_list = decoded_string.split(',')

    decoded_dictionary = {}
    instance = None
    second_instance = 0
    position = None

    for item in range(len(decoded_list)):
        if decoded_list[item] == 'temp':
            decoded_dictionary['temp'] = {}
            instance = 'temp'
            continue

        if decoded_list[item] == 'ir':
            decoded_dictionary['ir'] = {}
            instance = 'ir'
            continue

        if decoded_list[item] == 'gyro':
            decoded_dictionary['gyro'] = {}
            instance = 'gyro'
            continue

        if decoded_list[item] == 'grayscale':
            decoded_dictionary['grayscale'] = {}
            instance = 'grayscale'
            continue

        if decoded_list[item] == 'encoder':
            decoded_dictionary['encoder'] = {}
            instance = 'encoder'
            continue

        if instance == 'temp':
            if second_instance == 0:
                position = 'left_back'
                second_instance += 1
            elif second_instance == 1:
                position = 'left_front'
                second_instance += 1
            elif second_instance == 2:
                position = 'right_front'
                second_instance += 1
            elif second_instance == 3:
                position = 'right_back'
                second_instance = 0
            decoded_dictionary['temp'][position] = float(decoded_list[item])
            continue

        if instance == 'ir':
            if second_instance == 0:
                position = 'left_back'
                second_instance += 1
            elif second_instance == 1:
                position = 'left_front'
                second_instance += 1
            elif second_instance == 2:
                position = 'front_left'
                second_instance += 1
            elif second_instance == 3:
                position = 'front_right'
                second_instance += 1
            elif second_instance == 4:
                position = 'right_front'
                second_instance += 1
            elif second_instance == 5:
                position = 'right_back'
                second_instance = 0
            decoded_dictionary['ir'][position] = float(decoded_list[item])
            continue

        if instance == 'gyro':
            if second_instance == 0:
                position = 'tilt'
                second_instance += 1
            elif second_instance == 1:
                position = 'rotation'
                second_instance = 0
            decoded_dictionary['gyro'][position] = float(decoded_list[item])
            continue

        if instance == 'grayscale':
            if second_instance == 0:
                position = 'grayscale'
                second_instance = 0
            decoded_dictionary['grayscale'][position] = float(decoded_list[item])
            continue

        if instance == 'encoder':
            if second_instance == 0:
                position = 'left_back'
                second_instance += 1
            elif second_instance == 1:
                position = 'left_front'
                second_instance += 1
            elif second_instance == 2:
                position = 'right_front'
                second_instance += 1
            elif second_instance == 3:
                position = 'right_back'
                second_instance = 0
            decoded_dictionary['encoder'][position] = float(decoded_list[item])
            continue

    return decoded_dictionary


def analyze(data, which_type):
    if which_type == 'all':
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
            walls['rigth'] = 1
        else:
            walls['rigth'] = 0

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
            walls['rigth'] = 1
        else:
            walls['rigth'] = 0
        walls['back'] = 0

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
