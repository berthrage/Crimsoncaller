from PPlay.sprite import *
from PPlay.collision import *
from Enemy import *
from GameWindow import *
import Player as Pl
import Game

class Devotee(Enemy):
    def __init__(self, sprite=Sprite("sprites/enemies/devotee.png", 8), health=100):
        super().__init__(sprite, health)
        self.sprite = Sprite("sprites/enemies/devotee2.png", 8)
        self.sprite.set_sequence_time(0, 8, 100, True)


