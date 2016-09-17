from inputs import get_key
from _thread import start_new_thread

key = {}

def get_all_keys():
    while True:
        events = get_key()
        for event in events:
            if event.ev_type == "Key":        
                key[event.code] = event.state

start_new_thread(get_all_keys, ())

class Key():
    def __init__(self, key_code):
        self.key_code = key_code

    @property
    def state(self):
        return key.get(self.key_code, 0)

    @property
    def pressed(self):
        return ((self.state == 1) or (self.state == 2))

    @property
    def held(self):
        return (self.state == 2)

    def when_pressed(self, my_function):
        pass
        
    def when_held(self, my_function):
        pass

    def when_released(self, my_function):
        pass

def is_key_pressed(what_key):
    what_key = "KEY_" + what_key.upper()
    return (key.get(what_key, 0) != 0)


key_a = Key("KEY_A")
key_b = Key("KEY_B")
key_c = Key("KEY_C")
key_d = Key("KEY_D")
key_e = Key("KEY_E")
key_f = Key("KEY_F")
key_g = Key("KEY_G")
key_h = Key("KEY_H")
key_i = Key("KEY_I")
key_j = Key("KEY_J")
key_k = Key("KEY_K")
key_l = Key("KEY_L")
key_m = Key("KEY_M")
key_n = Key("KEY_N")
key_o = Key("KEY_O")
key_p = Key("KEY_P")
key_q = Key("KEY_Q")
key_r = Key("KEY_R")
key_s = Key("KEY_S")
key_t = Key("KEY_T")
key_u = Key("KEY_U")
key_v = Key("KEY_V")
key_w = Key("KEY_W")
key_x = Key("KEY_X")
key_y = Key("KEY_Y")
key_z = Key("KEY_Z")
key_1 = Key("KEY_1")
key_2 = Key("KEY_2")
key_3 = Key("KEY_3")
key_4 = Key("KEY_4")
key_5 = Key("KEY_5")
key_6 = Key("KEY_6")
key_7 = Key("KEY_7")
key_8 = Key("KEY_8")
key_9 = Key("KEY_9")
key_0 = Key("KEY_0")
key_space = Key("KEY_SPACE")
key_leftshift = Key("KEY_LEFTSHIFT")
key_leftshift = Key("KEY_RIGHTSHIFT")
key_esc = Key("KEY_ESC")
key_leftctrl = Key("KEY_LEFTCTRL")
key_rightctrl = Key("KEY_RIGHTCTRL")
