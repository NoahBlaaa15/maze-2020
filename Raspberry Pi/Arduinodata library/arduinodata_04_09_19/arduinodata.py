#Arduinodata library
#TODO:
#Dictionaryeinträge zu eigenen, 1 Item Dictionarys machen(-> data['temp']['leftback'] für Wert des Thermometers links hinten)

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
    
    for item in range(len(decoded_list)):
        if decoded_list[item] == 'temp':
            decoded_dictionary['temp'] = []
            instance = 'temp'
            continue

        if decoded_list[item] == 'ir':
            decoded_dictionary['ir'] = []
            instance = 'ir'
            continue

        if decoded_list[item] == 'gyro':
            decoded_dictionary['gyro'] = []
            instance = 'gyro'
            continue

        if decoded_list[item] == 'grayscale':
            decoded_dictionary['grayscale'] = []
            instance = 'grayscale'
            continue

        if decoded_list[item] == 'encoder':
            decoded_dictionary['encoder'] = []
            instance = 'encoder'
            continue
            
        if instance == 'temp':
            decoded_dictionary['temp'].append(float(decoded_list[item]))
            continue

        if instance == 'ir':
            decoded_dictionary['ir'].append(float(decoded_list[item]))
            continue

        if instance == 'gyro':
            decoded_dictionary['gyro'].append(decoded_list[item])
            continue

        if instance == 'grayscale':
            decoded_dictionary['grayscale'].append(float(decoded_list[item]))
            continue

        if instance == 'encoder':
            decoded_dictionary['encoder'].append(float(decoded_list[item]))
            continue

    return decoded_dictionary
