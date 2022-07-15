from Enemy import *
from Animations import AnimatedSprite

class Devotee(Enemy):
    def __init__(self, positionX, positionY, direction='left', health=100):
        super().__init__(positionX, positionY, health)
        self.health = health
        self.damage = 25
        self.sprite = Sprite("sprites/enemies/devotee2/1.png")
        self.direction = direction
        self.pray = True
        self.attack = False

        self.animatedSprites = []

        self.prayAnim = AnimatedSprite()
        self.prayAnim.addSprite("sprites/enemies/devotee2", 8)
        self.animatedSprites.append(self.prayAnim)


    def praying(self, direction):
        if (self.direction == direction and
            self.pray):
            return True
        else:
            return False

    def animationController(self):
        from Player import Player
        if not self.dead:
            if self.praying('left'):
                self.prayAnim.playAnimation(self.sprite, 8, self.animatedSprites)
            elif self.praying('right'):
                self.prayAnim.playAnimationFlipped(self.sprite, 8, self.animatedSprites)
            if self.health <= 0:
                Player.health += 10