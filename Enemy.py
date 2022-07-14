from PPlay.sprite import *
from GameWindow import *
import Player as Pl
import Levels

allEnemies = []

class Enemy():
    def __init__(self, positionX, positionY,sprite=Sprite("sprites/player/right/julius-jumpmid-still-right.png", 2), health=100):
        self.health = 100
        self.sprite = Sprite("sprites/player/right/julius-jumpmid-still-right.png", 2)
        self.sprite.set_sequence_time(0, 2, 40, True)
        self.posSet = False
        self.mostrarHealth = False
        self.mostrarHealthTimer = Misc.Timer()
        self.walking = False
        self.attack = False
        self.dead = False
        self.initialPositionX = positionX
        self.initialPositionY = positionY

        self.interval = 0.5
        self.increment = 0.05
        self.step = 0.05
        self.show = True
        self.clock = 0

        self.deathInterval = 3
        self.deathTimer = Misc.Timer()
        self.deathAnimationPlayed = False

    def spawn(self):

        self.deadState()
        self.moveAccordingLevelScrolling(self.sprite)

        if (not self.posSet):
            # self.sprite = Sprite("sprites/enemies/devotee.png", 8)
            # self.sprite.set_sequence_time(0, 8, 40, True)
            self.sprite.set_position(self.initialPositionX, self.initialPositionY)
            self.posSet = True

        if not self.dead:
            #self.sprite.draw()
            #self.sprite.update()
            self.collision()
            self.showHealth()



    def move(self):
        self.sprite.x += 100 * GameWindow.window.delta_time()

    def moveAccordingLevelScrolling(self, sprite):
        from Game import Game

        if (Pl.Player.direction == 2):
            if (Pl.Player.sprite.x > Game.currentLevel.scrollingLimit and not Pl.Player.still and not Pl.Player.collidedWall and not Game.currentLevel.reachedLimitRight):
                sprite.x -= Pl.Player.currentSpeed * GameWindow.window.delta_time()
        elif (Pl.Player.direction == 1):
            if (Pl.Player.sprite.x < Game.currentLevel.scrollingLimit and not Pl.Player.still and not Pl.Player.collidedWall and not Game.currentLevel.reachedLimitLeft):
                sprite.x += Pl.Player.currentSpeed * GameWindow.window.delta_time()

    def collision(self):
        if self.sprite.collided_perfect(Pl.Player.sprite) and Pl.Player.attacking and self.ready:
            self.health -= 25
            self.mostrarHealth = True
            self.ready = False
        else:
            if not Pl.Player.attacking:
                self.ready = True

        if self.sprite.collided_perfect(Pl.Player.sprite) and self.attack and self.clock <= 0 :
            Pl.Player.health -= self.damage
            self.clock = 1
        else:
            self.clock -= GameWindow.window.delta_time()

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

    def deadState(self):
        if(self.health <= 0):
            self.dead = True

        if(self.dead and not self.deathAnimationPlayed):
            self.deathTimer.resumeTimer()
            self.deathTimer.executeTimer()

            if (self.deathTimer.time >= self.deathInterval):
                self.sprite.x += 9999
                self.sprite.y -= 9999
                self.deathAnimationPlayed = True
                self.deathTimer.stopTimer()
                self.deathTimer.resetTimer()

            #allEnemies.pop(self)
