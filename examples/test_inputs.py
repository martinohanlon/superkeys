
from inputs import get_key
from time import sleep
    
while True:
    events = get_key()
    if events:
        for event in events:
            print(event.ev_type, event.code, event.state)
