import sys
import arduinodata

examplestring = '''
{
  "temp": [
    "12",
    "12",
    "12",
    "12"
  ],
  "ir": [
    "20",
    "20",
    "20",
    "20",
    "20",
    "20"
  ],
  "gyro": [
    "50",
    "227"
    ],
  "grayscale": "0.5",
  "encoder": [
    "5",
    "5",
    "50",
    "5"
  ]
}
'''

data = arduinodata.decode(examplestring)
print(data)
print('\n')
for i in data:
    print(i, data[i])

walls = arduinodata.analyze(data, 'walls')
for i in walls:
    print(i, walls[i])

victims = arduinodata.analyze(data, 'victims')
for i in victims:
    print(i, victims[i])

environment = arduinodata.analyze(data, 'environment')
for i in environment:
    print(i, environment[i])

motors = arduinodata.analyze(data, 'motors')
for i in motors:
    print(i, motors[i])

print('ALL')

wallsdata, victimsdata, environmentdata, motorsdata = arduinodata.analyze(data, 'all')
for i in wallsdata:
    print(i, wallsdata[i])
for i in victimsdata:
    print(i, victimsdata[i])
for i in environmentdata:
    print(i, environmentdata[i])
for i in motorsdata:
    print(i, motorsdata[i])
input('Waiting')
