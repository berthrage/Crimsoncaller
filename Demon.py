from Enemy import *
from Animations import AnimatedSprite
from PPlay.sprite import *
from GameWindow import *
from Enemy import allEnemies

class Demon(Enemy):
    def __init__(self, positionX, positionY, direction='left', health=100):
        super().__init__(positionX, positionY, health)
        self.health = health
        self.speed = 150
        self.damage = 25
        self.direction = direction
        self.walk = True
        self.attack = False
        self.readyToDie = True
        self.sprite = Sprite("sprites/enemies/demon/walking/1.png")
        self.tick = 1

        self.animatedSprites = []

        self.walkingAnim = AnimatedSprite()
        self.walkingAnim.addSprite("sprites/enemies/demon/walking", 6)
        self.animatedSprites.append(self.walkingAnim)

        self.attackingAnim = AnimatedSprite()
        self.attackingAnim.addSprite("sprites/enemies/demon/attacking", 4)
        self.animatedSprites.append(self.attackingAnim)

        self.dyingAnim = AnimatedSprite()
        self.dyingAnim.addSprite("sprites/enemies/demon/death", 10)
        self.animatedSprites.append(self.dyingAnim)


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


    def dying(self, direction):
        if (self.direction == direction and
        self.readyToDie):
            return True
        else:
            return False


    def movController(self):
        from Player import Player

        if self.andando('left'):
            self.sprite.x -= GameWindow.window.delta_time() * self.speed
            if self.sprite.x <= Player.sprite.x - 25 :
                self.walk = False
                self.attack = True
                self.sprite.x += 25

        elif self.andando('right'):
            self.sprite.x += GameWindow.window.delta_time() * self.speed
            if self.sprite.x >= Player.sprite.x - 150 :
                self.walk = False
                self.attack = True
                #self.sprite.x -= 25

        elif self.atacando('left'):
            if not (self.sprite.x <= Player.sprite.x ) :
                self.attack = False
                self.walk = True

        elif self.atacando('right'):
            if not (self.sprite.x >= Player.sprite.x - 150):
                self.attack = False
                self.walk = True


    def animationController(self):
        from Player import Player

        if not self.dead:

            if self.andando('left'):
                self.walkingAnim.playAnimationFlipped(self.sprite, 6, self.animatedSprites)
            elif self.andando('right'):
                self.walkingAnim.playAnimation(self.sprite, 6, self.animatedSprites)
            
            elif self.atacando('left'):
                self.attackingAnim.playAnimationFlipped(self.sprite, 4, self.animatedSprites)
            elif self.atacando('right'):
                self.attackingAnim.playAnimation(self.sprite, 4, self.animatedSprites)

            if  self.direction == 'right' and self.sprite.x >= Player.sprite.x + 25:
                self.direction = 'left'

            elif self.direction == 'left' and self.sprite.x <= Player.sprite.x - 25:
                self.direction = 'right'

            self.movController()

        elif self.dying('left') and self.tick >= 0:
            self.dyingAnim.playAnimationFlipped(self.sprite, 10, self.animatedSprites)
            self.tick -= GameWindow.window.delta_time()
            #if self.dyingAnim.currentFrame >= 4:
            #    self.readyToDie = False
        elif self.dying('right') and self.tick >= 0:
            self.dyingAnim.playAnimation(self.sprite, 10, self.animatedSprites)
            self.tick -= GameWindow.window.delta_time()
            #if self.dyingAnim.currentFrame >= 4:
            #    self.readyToDie = False