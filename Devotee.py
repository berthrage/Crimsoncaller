from PPlay.sprite import *
import Game

class Devotee:
    def __init__(self, sprite=Sprite("sprites/enemies/devotee.png", 8), health=100):
        self.sprite = Sprite("sprites/enemies/devotee.png", 8)
        self.health = 100

        self.sprite.set_position(600, 465)



    def spawn(self):
        self.sprite.draw()
        self.sprite.set_sequence_time(0, 8, 40, True)
        self.sprite.update()
