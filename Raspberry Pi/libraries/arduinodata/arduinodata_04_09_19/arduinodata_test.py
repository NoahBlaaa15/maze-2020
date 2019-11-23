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
  "gyro": "ka",
  "grayscale": "0.5",
  "encoder": [
    "5",
    "5",
    "5",
    "5"
  ]
}
'''

data = arduinodata.decode(examplestring)
print(data)
print('\n')
for i in data:
    print(i, data[i])
input('Waiting')
