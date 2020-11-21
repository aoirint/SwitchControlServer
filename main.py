import time
import json
from serial import Serial, SerialTimeoutException

serial = Serial(
    port='/dev/ttyUSB0',
    baudrate=1200,
    timeout=1.0,
    write_timeout=1.0,
)

print('Connecting')
time.sleep(3.0)

def send(data):
    string = json.dumps(data) + '\n'
    serial.write(string.encode(encoding='ascii'))

    # reply
    try:
        print(serial.readline().decode(encoding='ascii'))
    except UnicodeDecodeError as err:
        print(err)

data = {
    'button': 0,
    'hat': 0x08,
    'leftX': 127,
    'leftY': 127,
    'rightX': 127,
    'rightY': 127,
}

while True:
    print('Neutral')
    data['leftX'] = 127
    send(data)
    time.sleep(0.5)

    print('Left')
    data['leftX'] = 0
    send(data)
    time.sleep(0.5)

    print('Neutral')
    data['leftX'] = 127
    send(data)
    time.sleep(0.5)

    print('Right')
    data['leftX'] = 255
    send(data)
    time.sleep(0.5)
