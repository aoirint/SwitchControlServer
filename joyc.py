# for test

import time
from pyjoycon import JoyCon, get_L_id, get_R_id

joycon_l_id = get_L_id()
joycon_r_id = get_R_id()

joycon_l = JoyCon(*joycon_l_id)
joycon_r = JoyCon(*joycon_r_id)

while True:
    print(joycon_l.get_status())
    print(joycon_r.get_status())

    print(int(joycon_l.get_stick_left_horizontal() / 4096 * 255))
    print(int(joycon_l.get_stick_left_vertical() / 4096 * 255))
