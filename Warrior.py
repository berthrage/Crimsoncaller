from Enemy import *
from Animations import AnimatedSprite
from PPlay.sprite import *
from GameWindow import *
from Player import *

class Warrior(Enemy):
    def __init__(self, direction, health = 100):
        super().__init__(health)
        self.health = health
        self.speed = 150
        self.damage = 25
        self.direction = direction
        self.start = True
        self.walk = False
        self.attack = False
        self.sprite = Sprite("sprites/enemies/warrior/left/starting/1.png")

    animatedSprites = []

    startAnim = AnimatedSprite()
    startAnim.addSprite("sprites/enemies/warrior/left/starting", 8)
    animatedSprites.append(startAnim)

    walkingAnim = AnimatedSprite()
    walkingAnim.addSprite("sprites/enemies/warrior/left/walking", 5)
    animatedSprites.append(walkingAnim)

    attackingAnim = AnimatedSprite()
    attackingAnim.addSprite("sprites/enemies/warrior/left/attacking", 5)
    animatedSprites.append(attackingAnim)

    @staticmethod
    def starting(self, direction):
        if (self.direction == direction and
                self.start):
            return True
        else:
            return False

    @staticmethod
    def andando(self, direction):
        if (self.direction == direction and
        self.walk):
            return True
        else:
            return False

    @staticmethod
    def atacando(self, direction):
        if (self.direction == direction and
        self.attack):
            return True
        else:
            return False

    @staticmethod
    def movController(self):
        if self.start:
            if self.startAnim.currentFrame >= 4:
                self.start = False
                self.walk = True

        elif self.andando(self,'left'):
                self.sprite.x -= self.speed * GameWindow.window.delta_time()
                if self.sprite.x <= Player.sprite.x + 100:
                    self.walk = False
                    self.attack = True
                    self.sprite.x -= 25
        elif self.andando(self,'right'):
            self.sprite.x += self.speed * GameWindow.window.delta_time()
            if self.sprite.x >= Player.sprite.x:
                self.walk = False
                self.attack = True
                self.sprite.x += 25

        elif self.atacando(self, 'left'):
            if  not self.sprite.x <= Player.sprite.x + 100:
                    self.walk = True
                    self.attack = False
        elif self.atacando(self, 'right'):
            if not self.sprite.x >= Player.sprite.x - 100:
                self.walk = False
                self.attack = True

    @staticmethod
    def animationController(self):
        if not self.dead:

            if self.starting(self,'left'):
                self.startAnim.playAnimation(self.sprite, 8, self.animatedSprites)
            elif self.starting(self,'right'):
                self.startAnim.playAnimationFlipped(self.sprite, 8, self.animatedSprites)

            elif self.atacando(self, 'left'):
                self.attackingAnim.playAnimation(self.sprite, 5, self.animatedSprites)
            elif self.atacando(self, 'right'):
                self.attackingAnim.playAnimationFlipped(self.sprite, 5, self.animatedSprites)

            elif self.andando(self,'left'):
                self.walkingAnim.playAnimation(self.sprite, 7, self.animatedSprites)
            elif self.andando(self,'right'):
                self.walkingAnim.playAnimationFlipped(self.sprite, 7, self.animatedSprites)

            if  self.direction == 'right' and self.sprite.x >= Player.sprite.x + 25:
                self.direction = 'left'

            elif self.direction == 'left' and self.sprite.x <= Player.sprite.x - 25:
                self.direction = 'right'
            
            self.movController(self)
