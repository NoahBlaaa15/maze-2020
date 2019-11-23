#MAZE 2020 ALLA

import maze_serial as m_ser
import time

m_ser.start

while True:
    m_ser.send('pls#')
    data = m_ser.receive()
    print(data)
    time.sleep(1)
