import time
import json
from serial import Serial, SerialTimeoutException


from pyjoycon import JoyCon, get_L_id, get_R_id

joycon_l_id = get_L_id()
joycon_r_id = get_R_id()

joycon_l = JoyCon(*joycon_l_id)
joycon_r = JoyCon(*joycon_r_id)


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


# order is different from USB-HID
def get_button(joycon):
    return joycon.get_button_y() \
        | (joycon.get_button_b() << 1) \
        | (joycon.get_button_a() << 2) \
        | (joycon.get_button_x() << 3) \
        | (joycon.get_button_l() << 4) \
        | (joycon.get_button_r() << 5) \
        | (joycon.get_button_zl() << 6) \
        | (joycon.get_button_zr() << 7) \
        | (joycon.get_button_minus() << 8) \
        | (joycon.get_button_plus() << 9) \
        | (joycon.get_button_l_stick() << 10) \
        | (joycon.get_button_r_stick() << 11) \
        | (joycon.get_button_home() << 12) \
        | (joycon.get_button_capture() << 13)

# format is different from USB-HID
def get_hat(joycon):
    u = joycon.get_button_up() == 1
    r = joycon.get_button_right() == 1
    d = joycon.get_button_down() == 1
    l = joycon.get_button_left() == 1

    if u:
        if r:
            return 0x01
        if l:
            return 0x07
        return 0x00

    if d:
        if r:
            return 0x03
        if l:
            return 0x06
        return 0x04

    if r:
        return 0x02
    if l:
        return 0x06
    return 0x08

 # 12 -> 8 bit conversion & invert
def get_left_x(joycon):
    return int(joycon.get_stick_left_horizontal() / 4096 * 255)

def get_left_y(joycon):
    return int((4096 - joycon.get_stick_left_vertical()) / 4096 * 255)

def get_right_x(joycon):
    return int(joycon.get_stick_right_horizontal() / 4096 * 255)

def get_right_y(joycon):
    return int((4096 - joycon.get_stick_right_vertical()) / 4096 * 255)


while True:
    data['button'] = get_button(joycon_r)
    data['hat'] = get_hat(joycon_l)

    data['leftX'] = get_left_x(joycon_l)
    data['leftY'] = get_left_y(joycon_l)

    data['rightX'] = get_right_x(joycon_r)
    data['rightY'] = get_right_y(joycon_r)

    send(data)
    time.sleep(0.01)
