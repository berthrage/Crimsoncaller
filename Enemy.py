from PPlay.sprite import *
from GameWindow import *
import Player as Pl
import Levels

class Enemy():
    def __init__(self, sprite=Sprite("sprites/player/right/julius-jumpmid-still-right.png", 2), health=100):
        self.health = 100
        self.sprite = Sprite("sprites/player/right/julius-jumpmid-still-right.png", 2)
        self.sprite.set_sequence_time(0, 2, 40, True)
        self.posSet = False
        self.level = Levels.Level1area1
        self.mostrarHealth = False
        self.mostrarHealthTimer = Misc.Timer()

        self.walking = False
        self.attacking = False

    def spawn(self, positionX, positionY):
        self.sprite.draw()
        self.sprite.update()
        self.moveAccordingLevelScrolling()
        self.collision()
        self.showHealth()

        if (not self.posSet):
            # self.sprite = Sprite("sprites/enemies/devotee.png", 8)
            # self.sprite.set_sequence_time(0, 8, 40, True)
            self.sprite.set_position(positionX, positionY)
            self.posSet = True

    def move(self):
        self.sprite.x += 100 * GameWindow.window.delta_time()

    def moveAccordingLevelScrolling(self):
        if (Pl.Player.direction == 2):
            if (Pl.Player.sprite.x > self.level.scrollingLimit and not Pl.Player.still and not self.level.reachedLimitRight):
                self.sprite.x -= Pl.Player.currentSpeed * GameWindow.window.delta_time()
        elif (Pl.Player.direction == 1):
            if (Pl.Player.sprite.x < self.level.scrollingLimit and not Pl.Player.still and not self.level.reachedLimitLeft):
                self.sprite.x += Pl.Player.currentSpeed * GameWindow.window.delta_time()

    def collision(self):
        if self.sprite.collided_perfect(Pl.Player.sprite) and Pl.Player.attacking and self.ready:
            self.health -= 25
            self.mostrarHealth = True
            self.ready = False
            print('dano')
        else:
            if not Pl.Player.attacking:
                self.ready = True

    def showHealth(self):
        if (self.mostrarHealth):
            GameWindow.window.draw_text('-25', self.sprite.x, self.sprite.y, 90, [255, 0, 0],
                                        "fonts/AncientModernTales.ttf", False, False, False)
            self.mostrarHealthTimer.resumeTimer()
            self.mostrarHealthTimer.executeTimer()

            if (self.mostrarHealthTimer.time >= 0.5):
                self.mostrarHealth = False
                self.mostrarHealthTimer.stopTimer()
                self.mostrarHealthTimer.resetTimer()

