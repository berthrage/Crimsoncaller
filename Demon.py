from Enemy import *
from Animations import AnimatedSprite
from PPlay.sprite import *
from GameWindow import *
from Player import *
from Enemy import allEnemies

class Demon(Enemy):
    def __init__(self, direction, health=100):
        super().__init__(health)
        self.health = health
        self.speed = 150
        self.damage = 25
        self.direction = direction
        self.walk = True
        self.attack = False
        self.readyToDie = True
        self.sprite = Sprite("sprites/enemies/demon/walking/1.png")
        self.tick = 1

    animatedSprites = []

    walkingAnim = AnimatedSprite()
    walkingAnim.addSprite("sprites/enemies/demon/walking", 6)
    animatedSprites.append(walkingAnim)

    attackingAnim = AnimatedSprite()
    attackingAnim.addSprite("sprites/enemies/demon/attacking", 4)
    animatedSprites.append(attackingAnim)

    dyingAnim = AnimatedSprite()
    dyingAnim.addSprite("sprites/enemies/demon/death", 6)
    animatedSprites.append(dyingAnim)

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
    def dying(self, direction):
        if (self.direction == direction and
        self.readyToDie):
            return True
        else:
            return False

    @staticmethod
    def movController(self):
        if self.andando(self, 'left'):
            self.sprite.x -= GameWindow.window.delta_time() * self.speed
            if self.sprite.x <= Player.sprite.x - 25 :
                self.walk = False
                self.attack = True
                self.sprite.x += 25

        elif self.andando(self, 'right'):
            self.sprite.x += GameWindow.window.delta_time() * self.speed
            if self.sprite.x >= Player.sprite.x - 150 :
                self.walk = False
                self.attack = True
                #self.sprite.x -= 25

        elif self.atacando(self, 'left'):
            if not (self.sprite.x <= Player.sprite.x ) :
                self.attack = False
                self.walk = True

        elif self.atacando(self, 'right'):
            if not (self.sprite.x >= Player.sprite.x - 150):
                self.attack = False
                self.walk = True

    @staticmethod
    def animationController(self):
        if not self.dead:

            if self.andando(self, 'left'):
                self.walkingAnim.playAnimationFlipped(self.sprite, 6, self.animatedSprites)
            elif self.andando(self, 'right'):
                self.walkingAnim.playAnimation(self.sprite, 6, self.animatedSprites)
            
            elif self.atacando(self, 'left'):
                self.attackingAnim.playAnimationFlipped(self.sprite, 4, self.animatedSprites)
            elif self.atacando(self, 'right'):
                self.attackingAnim.playAnimation(self.sprite, 4, self.animatedSprites)

            if  self.direction == 'right' and self.sprite.x >= Player.sprite.x + 25:
                self.direction = 'left'

            elif self.direction == 'left' and self.sprite.x <= Player.sprite.x - 25:
                self.direction = 'right'

            self.movController(self)

        elif self.dying(self, 'left') and self.tick >= 0:
            self.dyingAnim.playAnimationFlipped(self.sprite, 6, self.animatedSprites)
            self.tick -= GameWindow.window.delta_time()
            #if self.dyingAnim.currentFrame >= 4:
            #    self.readyToDie = False
        elif self.dying(self, 'right') and self.tick >= 0:
            self.dyingAnim.playAnimation(self.sprite, 6, self.animatedSprites)
            self.tick -= GameWindow.window.delta_time()
            #if self.dyingAnim.currentFrame >= 4:
            #    self.readyToDie = False