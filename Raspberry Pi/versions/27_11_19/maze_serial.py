#Maze 2020 Serial module

import serial
import time

sr = serial.Serial("/dev/ttyS0", 9600)

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
            break
