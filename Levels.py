import Player
from PPlay.sprite import *
from GameWindow import *
import Player

class Level:
    def __init__(self, background=Sprite("sprites/maps/1-1/1-1-background.png"), tiles=Sprite("sprites/maps/1-1/1-1-tiles.png")):
        self.background = Sprite("sprites/maps/1-1/1-1-background.png")
        self.tiles = Sprite("sprites/maps/1-1/1-1-tiles.png")

        self.scrollingLimit = 550
        self.reachedLimitRight = False
        self.reachedLimitLeft = False


class Levels:

    @staticmethod
    def spawnLevel(Level):
        Level.background.draw()
        Level.tiles.draw()
        Level.logic()
        #Levels.scrollLevel(Level)
        #Level.tiles.update()


class Level1area1(Level):
    def __init__(self, background=Sprite("sprites/maps/1-1/1-1-background.png"), tiles=Sprite("sprites/maps/1-1/1-1-tiles.png")):
        super().__init__(background, tiles)

class Level1area2(Level):
    def __init__(self):
        super().__init__()
        self.background = Sprite("sprites/maps/1-1/1-1-background.png")
        self.tiles = Sprite("sprites/maps/1-1/1-1-tiles.png")