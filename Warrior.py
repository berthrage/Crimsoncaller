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
        self.dead = False   
        self.direction = direction
        self.start = True
        self.walk = False
        self.attack = False
        self.sprite = Sprite("sprites/enemies/warrior/left/unsheathing/1.png")

    animatedSprites = []

    startAnim = AnimatedSprite()
    startAnim.addSprite("sprites/enemies/warrior/left/unsheathing", 5)
    animatedSprites.append(startAnim)

    walkingAnim = AnimatedSprite()
    walkingAnim.addSprite("sprites/enemies/warrior/left/walking", 7)
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
    def walking(self, direction):
        if (self.direction == direction and
        self.walk):
            return True
        else:
            return False

    @staticmethod
    def attacking(self, direction):
        if (self.direction == direction and
        self.attack):
            return True
        else:
            return False

    @staticmethod
    def movController(self):
        if self.start:
            if self.startAnim.currentFrame >= 5:
                self.start = False
                self.walk = True

        elif self.walking(self,'left'):
                self.sprite.x -= self.speed * GameWindow.window.delta_time()
                if self.sprite.x <= Player.sprite.x + 100:
                    self.walk = False
                    self.attacking = True
        elif self.walking(self,'right'):
            self.sprite.x += self.speed * GameWindow.window.delta_time()
            if self.sprite.x >= Player.sprite.x - 100:
                self.walk = False
                self.attacking = True

        elif self.attacking(self, 'left'):
            if  not self.sprite.x <= Player.sprite.x + 100:
                    self.walk = True
                    self.attacking = False
        elif self.attacking(self, 'right'):
            if not self.sprite.x >= Player.sprite.x - 100:
                self.walk = False
                self.attacking = True

    @staticmethod
    def animationController(self):
        if not self.dead:

            if self.starting(self,'left'):
                self.startAnim.playAnimation(self.sprite, 5, self.animatedSprites)
            elif self.starting(self,'right'):
                self.startAnim.playAnimationFlipped(self.sprite, 5, self.animatedSprites)

            elif self.attacking(self, 'left'):
                self.attackingAnim.playAnimation(self.sprite, 5, self.animatedSprites)
            elif self.attacking(self, 'right'):
                self.attackingAnim.playAnimationFlipped(self.sprite, 5, self.animatedSprites)

            elif self.walking(self,'left'):
                self.walkingAnim.playAnimation(self.sprite, 7, self.animatedSprites)
            elif self.walking(self,'right'):
                self.walkingAnim.playAnimationFlipped(self.sprite, 7, self.animatedSprites)
            
            self.movController(self)
