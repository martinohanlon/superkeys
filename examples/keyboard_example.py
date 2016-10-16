"""Simple example showing how to get keyboard events."""

from __future__ import print_function

from inputs import get_key, devices
from time import sleep

from threading import Thread

def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    class InterruptableThread(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = default

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return default
    else:
        return it.result


def main():
    """Just print out some event infomation when keys are pressed."""
    while 1:
        #print("hi")
        #print(devices.keyboards[0]._do_iter())
        
        events = timeout(get_key, timeout_duration = 0.1)
        
        if events:
            
            if len(events) > 0:
                for event in events:
                    print(event.ev_type, event.code, event.state)
            else:
                print("none")
        

if __name__ == "__main__":
    main()
