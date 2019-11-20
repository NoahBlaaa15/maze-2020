#MAZE 2020 ALLA

import maze_serial as m_ser

m_ser.start

while True:
    m_ser.send('pls#')
    data = m_ser.receive('here')
    print(data)
