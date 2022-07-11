from Enemy import *
from Animations import AnimatedSprite

class Devotee(Enemy):
    def __init__(self, direction, health=50):
        super().__init__(health)
        self.health = health
        self.dead = False
        self.sprite = Sprite("sprites/enemies/devotee2/1.png")
        self.direction = direction
        self.pray = True

    animatedSprites = []

    prayAnim = AnimatedSprite()
    prayAnim.addSprite("sprites/enemies/devotee2", 8)
    animatedSprites.append(prayAnim)

    @staticmethod
    def praying(self, direction):
        if (self.direction == direction and
            self.pray):
            return True
        else:
            return False

    @staticmethod
    def animationController(self):
        if not self.dead:
            if self.praying(self,'left'):
                self.prayAnim.playAnimation(self.sprite, 8, self.animatedSprites)
            elif self.praying(self,'right'):
                self.prayAnim.playAnimationFlipped(self.sprite, 8, self.animatedSprites)