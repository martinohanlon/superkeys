from superkeys import *
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

while True:
    
    if is_key_pressed("t"):
        pos = mc.player.getTilePos()
        pos.y = pos.y - 1
        mc.setBlock(pos, block.TNT.id, 1)

    print("t {} ".format(key_t.pressed))


