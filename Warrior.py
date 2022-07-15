from Enemy import *
from Animations import AnimatedSprite
from PPlay.sprite import *
from GameWindow import *


class Warrior(Enemy):
    def __init__(self, positionX, positionY, direction='left', health = 100):
        super().__init__(positionX, positionY, health)
        self.health = health
        self.speed = 150
        self.damage = 10
        self.direction = direction
        self.detected = False
        self.esperando = True
        self.start = False
        self.walk = False
        self.attack = False
        self.sprite = Sprite("sprites/enemies/warrior/left/starting/1.png")

        self.animatedSprites = []

        self.startAnim = AnimatedSprite()
        self.startAnim.addSprite("sprites/enemies/warrior/left/starting", 8)
        self.animatedSprites.append(self.startAnim)

        self.walkingAnim = AnimatedSprite()
        self.walkingAnim.addSprite("sprites/enemies/warrior/left/walking", 5)
        self.animatedSprites.append(self.walkingAnim)

        self.attackingAnim = AnimatedSprite()
        self.attackingAnim.addSprite("sprites/enemies/warrior/left/attacking", 5)
        self.animatedSprites.append(self.attackingAnim)


    def detectado(self):
        from Player import Player
        if (self.sprite.x - Player.sprite.x <= 350):
            self.detected = True
            self.esperando = False
            self.walk = True

    def starting(self, direction):
        if (self.direction == direction and
                self.start):
            return True
        else:
            return False


    def andando(self, direction):
        if (self.direction == direction and
        self.walk):
            return True
        else:
            return False


    def atacando(self, direction):
        if (self.direction == direction and
        self.attack):
            return True
        else:
            return False

    def movController(self):
        from Player import Player

        if self.esperando:
            self.detectado()

        elif self.start:
            if self.startAnim.currentFrame >= 7:
                self.start = False
                self.walk = True

        elif self.andando('left'):
                self.sprite.x -= self.speed * GameWindow.window.delta_time()

                if self.sprite.x <= Player.sprite.x + 100:
                    self.walk = False
                    self.attack = True
                    self.sprite.x -= 25

        elif self.andando('right'):
            self.sprite.x += self.speed * GameWindow.window.delta_time()
            if self.sprite.x + self.sprite.width >= Player.sprite.x:
                self.walk = False
                self.attack = True

        elif self.atacando('left'):
            if  not self.sprite.x <= Player.sprite.x + 100:
                    self.walk = True
                    self.attack = False

        elif self.atacando('right'):
            if not self.sprite.x >= Player.sprite.x - 100:
                self.walk = True
                self.attack = False

    def animationController(self):
        from Player import Player
        if not self.dead:

            if self.esperando:
                self.sprite.draw()

            elif self.starting('left'):
                self.startAnim.playAnimation(self.sprite, 8, self.animatedSprites)
            elif self.starting('right'):
                self.startAnim.playAnimationFlipped(self.sprite, 8, self.animatedSprites)

            elif self.atacando('left'):
                self.attackingAnim.playAnimation(self.sprite, 5, self.animatedSprites)
            elif self.atacando('right'):
                self.attackingAnim.playAnimationFlipped(self.sprite, 5, self.animatedSprites)

            elif self.andando('left'):
                self.walkingAnim.playAnimation(self.sprite, 7, self.animatedSprites)
            elif self.andando('right'):
                self.walkingAnim.playAnimationFlipped(self.sprite, 7, self.animatedSprites)

            else:
                self.startAnim.playAnimation(self.sprite, 8, self.animatedSprites)

            if  self.direction == 'right' and self.sprite.x >= Player.sprite.x + 100:
                self.direction = 'left'

            elif self.direction == 'left' and self.sprite.x <= Player.sprite.x - 100:
                self.direction = 'right'
            
            self.movController()