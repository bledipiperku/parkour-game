from ursina import *
import sys
sys.path.append('../Parkour/')
from block import *

normalSpeed = 2
boostSpeed  = 5
normalJump = 0.3

# Level08
class Level08(Entity):
    def __init__(self):
        super().__init__()

        self.is_enabled = False

        self.block_8_1 = NormalBlock((0, 9, 0))
        self.block_8_2 = NormalBlock((0, 10, 20))
        self.block_8_3 = NormalBlock((0, 15, 40))

        self.block_8_4 = JumpBlock((0, 40, 75))
        self.block_8_5 = JumpBlock((0, -40, 130))
        self.block_8_6 = JumpBlock((0, -40, 185))
        self.block_8_7 = JumpBlock((0, -40, 240))
        self.block_8_8 = JumpBlock((0, -40, 295))

        self.block_8_9 = SpeedBlock((0, 0, 320), (0, 90, 0))
        self.block_8_10 = SpeedBlock((0, 0, 370), (0, 90, 0))
        self.block_8_11 = SpeedBlock((0, 0, 425), (0, 90, 0))
        
        self.block_8_12 = NormalBlock((0, 0, 475))
        self.block_8_13 = NormalBlock((0, 1, 495))
        self.block_8_14 = NormalBlock((0, 2, 515))
        self.block_8_15 = NormalBlock((20, 3, 515))
        self.block_8_16 = NormalBlock((40, 4, 515))
        self.block_8_17 = NormalBlock((40, 5, 495))
        self.block_8_18 = NormalBlock((40, 6, 475))
        self.block_8_19 = NormalBlock((40, 6, 450), scale = (2, 2, 2))

        self.finishBlock_8 = EndBlock((40, 8, 450)) 

        self.player = None

        self.disable()

    def disable(self):
        self.is_enabled = False

        self.block_8_1.disable()
        self.block_8_2.disable()
        self.block_8_3.disable()
        self.block_8_4.disable()
        self.block_8_5.disable()
        self.block_8_6.disable()
        self.block_8_7.disable()
        self.block_8_8.disable()
        self.block_8_9.disable()
        self.block_8_10.disable()
        self.block_8_11.disable()
        self.block_8_12.disable()
        self.block_8_13.disable()
        self.block_8_14.disable()
        self.block_8_15.disable()
        self.block_8_16.disable()
        self.block_8_17.disable()
        self.block_8_18.disable()
        self.block_8_19.disable()

        self.finishBlock_8.disable()

    def enable(self):
        self.is_enabled = True

        self.block_8_1.enable()
        self.block_8_2.enable()
        self.block_8_3.enable()
        self.block_8_4.enable()
        self.block_8_5.enable()
        self.block_8_6.enable()
        self.block_8_7.enable()
        self.block_8_8.enable()
        self.block_8_9.enable()
        self.block_8_10.enable()
        self.block_8_11.enable()
        self.block_8_12.enable()
        self.block_8_13.enable()
        self.block_8_14.enable()
        self.block_8_15.enable()
        self.block_8_16.enable()
        self.block_8_17.enable()
        self.block_8_18.enable()
        self.block_8_19.enable()

        self.finishBlock_8.enable()

    def update(self):
        # Stops the player from falling forever
        if self.is_enabled == True and self.player.position.y <= -50:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (0, 10, 0)
            self.player.rotation = (0, 0, 0)
            self.player.count = 0.0

        # Restart the level
        if self.is_enabled == True and held_keys["g"]:
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.position = (0, 10, 0)
            self.player.rotation = (0, 0, 0)
            self.player.count = 0.0

        # What entity the player hits
        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])

        if hit.entity == self.block_8_1:
            self.player.jump_height = 0.5
        if hit.entity == self.block_8_3:
            self.player.jump_height = 1.2
        if hit.entity == self.block_8_4:
            self.player.jump_height = 1.2
        if hit.entity == self.block_8_5:
            self.player.jump_height = 1.2
        if hit.entity == self.block_8_6:
            self.player.jump_height = 1.2
        if hit.entity == self.block_8_7:
            self.player.jump_height = 1.2
        if hit.entity == self.block_8_8:
            self.player.jump_height = 1.2
        elif hit.entity == self.block_8_9:
            self.player.jump_height = normalJump
            self.player.SPEED = 5
        if hit.entity == self.block_8_10:
            self.player.SPEED = 6
        if hit.entity == self.block_8_11:
            self.player.SPEED = 7
        elif hit.entity == self.block_8_12:
            self.player.SPEED = normalSpeed
        elif hit.entity == self.block_8_13:
            self.player.SPEED = normalSpeed