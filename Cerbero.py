from Animations import AnimatedSprite
from Enemy import *
from PPlay.sprite import *
from GameWindow import *
from Player import *

class Cerbero(Enemy):
    def __init__(self, direction, health = 100):
        super().__init__(health)
        self.health = health
        self.speed = 150
        self.dead = False 
        self.damage = 25 
        self.direction = direction
        self.sprite = Sprite("sprites/enemies/cerbero/right/walking/1.png")
        self.walk = True

    animatedSprites = []

    walkingAnim = AnimatedSprite()
    walkingAnim.addSprite("sprites/enemies/cerbero/right/walking", 8)
    animatedSprites.append(walkingAnim)

    @staticmethod
    def walking(self, direction):
        if (self.direction == direction and
            self.walk):
            return True
        else:
            return False

    def movController(self):
        """ if (self.walking(self,'right')):
                self.sprite.x -= self.speed * GameWindow.window.delta_time()

        elif self.walking(self,'left'):
            self.sprite.x += self.speed * GameWindow.window.delta_time() """
        self.sprite.x -= self.speed * GameWindow.window.delta_time()

    @staticmethod
    def animationController(self):
        if not self.dead:

            """ if self.walking(self,'right'):
                self.walkingAnim.playAnimation(self.sprite, 7, self.animatedSprites)
            elif self.walking(self,'left'):
                self.walkingAnim.playAnimationFlipped(self.sprite, 7, self.animatedSprites) """
            self.walkingAnim.playAnimationFlipped(self.sprite, 7, self.animatedSprites)
            self.movController()
