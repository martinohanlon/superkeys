#A simple example which shows how to 

from superkeys import Key
a = Key("KEY_A")
b = Key("KEY_B")
while True:
    print("a {} b {}".format(a.pressed, b.pressed))  
