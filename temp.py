from PPlay.sprite import *
from PPlay.collision import *
from Enemy import *
from GameWindow import *
import Player as Pl
import Game

class Devotee(Enemy):
    def __init__(self, sprite=Sprite("sprites/enemies/devotee.png", 8), health=100):
        super().__init__(sprite, health)
        #self.sprite = Sprite("sprites/enemies/devotee2.png", 8)
        #self.sprite.set_sequence_time(0, 8, 100, True)

        self.sprites_off = []
        self.sprites_off.append(Sprite("sprites/enemies/devotee2/1.png"))
        self.sprites_off.append(Sprite("sprites/enemies/devotee2/2.png"))
        self.sprites_off.append(Sprite("sprites/enemies/devotee2/3.png"))
        self.sprites_off.append(Sprite("sprites/enemies/devotee2/4.png"))
        self.sprites_off.append(Sprite("sprites/enemies/devotee2/5.png"))
        self.sprites_off.append(Sprite("sprites/enemies/devotee2/6.png"))
        self.sprites_off.append(Sprite("sprites/enemies/devotee2/7.png"))
        self.sprites_off.append(Sprite("sprites/enemies/devotee2/8.png"))

        self.atual = 0
        self.sprite = self.sprites_off[0]
        #self.sprite.set_position(900, 450)
        self.off = False
        self.unsheathing = True

    def spawnDevotee(self, positionX, positionY):
        if (not self.posSet):
            self.sprite.set_position(positionX, positionY)
            self.posSet = True
        self.moveAccordingLevelScrolling(self.sprite)
        currentX = self.sprite.x
        currentY = self.sprite.y



        self.atual += 0.05
        if self.atual >= len(self.sprites_off):
            self.atual = 0
            self.unsheathing = False
            self.walking = True


        self.sprite = self.sprites_off[int(self.atual)]
        self.sprite.set_position(currentX, currentY)


        self.sprite.draw()

        #self.image.update()