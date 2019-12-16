#Maze 2020 Serial module

from serial import Serial

sr = Serial("/dev/ttyS0", 9600)


def start():
    sr.write('start#'.encode())


def send(message):
    encoded_message = message.encode()
    sr.write(encoded_message)


def receive():
    wholeMsg = ''
    while True:
        received_message = sr.read().decode()
        if received_message != '#':
            wholeMsg = wholeMsg + received_message
        else:
            return str(wholeMsg)
