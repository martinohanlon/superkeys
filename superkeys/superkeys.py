from inputs import get_key
from time import sleep
from threading import Thread
import atexit

key_refs = {}
key_state = {}

class KeyListener(Thread):
    def __init__(self):
        #setup threading
        Thread.__init__(self)
        self.running = False
        self.stopped = False
       
    def run(self):
        self.running = True
        self.stopped = False
        while not self.stopped:
            events = get_key()
            if events:
                for event in events:
                    if event.ev_type == "Key":
                        for key_ref in key_refs[event.code]:
                            key_ref.state = event.state
                        key_state[event.code] = event.state
            sleep(0.01)

        self.running = False
        
    def stop(self):
        self.stopped = False
        while self.running:
            sleep(0.01)
            
    def __del__(self):
        self.stop()

class Key():
    def __init__(self, key):
        self.key = key
        self.key_code = "KEY_" + key.upper()
        self._state = 0
        self._when_pressed = None
        
        #register object in key refs
        if self.key_code in key_refs:
            key_refs[self.key_code].append(self)
        else:
            key_refs[self.key_code] = [self]

    @property
    def state(self):
        return self._state
        
    @state.setter
    def state(self, value):
        self._state = value
        if value == 1 and self._when_pressed != None:
            self._when_pressed()

    @property
    def pressed(self):
        return ((self.state == 1) or (self.state == 2))

    @property
    def held(self):
        return (self.state == 2)

    @property
    def when_pressed(self):
        return self._when_pressed
        
    @when_pressed.setter
    def when_pressed(self, value):
        self._when_pressed = value
        
    def when_held(self, my_function):
        pass

    def when_released(self, my_function):
        pass

def is_key_pressed(what_key):
    what_key = "KEY_" + what_key.upper()
    return (key_state.get(what_key, 0) != 0)

# start the key listener
kl = KeyListener()
kl.start()

# register it to stop at exit
atexit.register(kl.stop)
key_a = Key("A")
key_b = Key("B")
key_c = Key("C")
key_d = Key("D")
key_e = Key("E")
key_f = Key("F")
key_g = Key("G")
key_h = Key("H")
key_i = Key("I")
key_j = Key("J")
key_k = Key("K")
key_l = Key("L")
key_m = Key("M")
key_n = Key("N")
key_o = Key("O")
key_p = Key("P")
key_q = Key("Q")
key_r = Key("R")
key_s = Key("S")
key_t = Key("T")
key_u = Key("U")
key_v = Key("V")
key_w = Key("W")
key_x = Key("X")
key_y = Key("Y")
key_z = Key("Z")
key_1 = Key("1")
key_2 = Key("2")
key_3 = Key("3")
key_4 = Key("4")
key_5 = Key("5")
key_6 = Key("6")
key_7 = Key("7")
key_8 = Key("8")
key_9 = Key("9")
key_0 = Key("0")
key_space = Key("SPACE")
key_leftshift = Key("LEFTSHIFT")
key_leftshift = Key("RIGHTSHIFT")
key_esc = Key("ESC")
key_leftctrl = Key("LEFTCTRL")
key_rightctrl = Key("RIGHTCTRL")

#test
if __name__ == "__main__":
    
    def myfunction():
        print("a pressed")
    
    key_a.when_pressed = myfunction
    
    while True:
        print("a state {}".format(key_a.state))
        print("b is pressed {}".format(is_key_pressed("b")))
        sleep(0.5)
