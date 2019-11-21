#Maze 2020 Serial module

import serial
import time

sr = serial.Serial("/dev/ttyS0", 9600)

def start():
    sr.write('start#'.encode())
    time.sleep(0.25)

def send(message):
    encoded_message = message.encode()
    sr.write(encoded_message)

def receive():
    completeMSG = ''
    while True:
        received_message = sr.read().decode()
        if received_message != '#':
            completeMSG = completeMSG + received_message
        else:
            return completeMSG
            break
