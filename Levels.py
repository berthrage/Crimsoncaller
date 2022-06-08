from PPlay.sprite import *

class Levels:

    @staticmethod
    def spawnLevel(Level):
        Level.background.draw()
        Level.tiles.draw()
        Level.logic()

class Level1area1:
    background = Sprite("sprites/maps/1-1/1-1-background.png")
    tiles = Sprite("sprites/maps/1-1/1-1-tiles.png")

    @staticmethod
    def logic():
        pass


