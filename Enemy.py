import Game
from PPlay.sprite import *
from GameWindow import *
import Levels
import Player

class Enemy():
    def __init__(self, sprite=Sprite("sprites/player/right/julius-jumpmid-still-right.png", 2), health=100):
        self.health = 100
        self.sprite = Sprite("sprites/player/right/julius-jumpmid-still-right.png", 2)
        self.sprite.set_sequence_time(0, 2, 40, True)
        self.posSet = False
        self.level = Game.Game.currentLevel


    def spawn(self, positionX, positionY):
        self.sprite.draw()
        self.sprite.update()
        self.moveAccordingLevelScrolling()

        if (not self.posSet):
            # self.sprite = Sprite("sprites/enemies/devotee.png", 8)
            # self.sprite.set_sequence_time(0, 8, 40, True)
            self.sprite.set_position(positionX, positionY)
            self.posSet = True

    def move(self):
        self.sprite.x += 100 * GameWindow.window.delta_time()

    def moveAccordingLevelScrolling(self):
        if (Player.Player.direction == 2):
            if (Player.Player.sprite.x > self.level.scrollingLimit and not Player.Player.still and not self.level.reachedLimitRight):
                self.sprite.x -= Player.Player.currentSpeed * GameWindow.window.delta_time()
        elif (Player.Player.direction == 1):
            if (Player.Player.sprite.x < self.level.scrollingLimit and not Player.Player.still and not self.level.reachedLimitLeft):
                self.sprite.x += Player.Player.currentSpeed * GameWindow.window.delta_time()

