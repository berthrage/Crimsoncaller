import Player
from PPlay.sprite import *
from GameWindow import *
import Player

class Levels:


    @staticmethod
    def spawnLevel(Level):
        Level.background.draw()
        Level.tiles.draw()
        Level.logic()
        Levels.scrollLevel(Level)
        #Level.tiles.update()

    @staticmethod
    def scrollLevel(Level):
        if(Level.tiles.x >= 0):
            Level.reachedLimitLeft = True
        else:
            Level.reachedLimitLeft = False

        if(Level.tiles.x <= -Level.tiles.width / 2):
            Level.reachedLimitRight = True
        else:
            Level.reachedLimitRight = False

        if(Player.Player.direction == 2):
            if(Player.Player.sprite.x > Level.scrollingLimit and not Player.Player.still and not Level.reachedLimitRight):
                Level.tiles.x -= Player.Player.currentSpeed * GameWindow.window.delta_time()
                Level.background.x -= (Player.Player.currentSpeed / 2) * GameWindow.window.delta_time()
        elif(Player.Player.direction == 1):
            if(Player.Player.sprite.x < Level.scrollingLimit and not Player.Player.still and not Level.reachedLimitLeft):
                Level.tiles.x += Player.Player.currentSpeed * GameWindow.window.delta_time()
                Level.background.x += (Player.Player.currentSpeed / 2) * GameWindow.window.delta_time()


class Level1area1:
    background = Sprite("sprites/maps/1-1/1-1-background.png")
    tiles = Sprite("sprites/maps/1-1/1-1-tiles.png")

    scrollingLimit = 550
    reachedLimitRight = False
    reachedLimitLeft = False

    @staticmethod
    def logic():
        pass

        
