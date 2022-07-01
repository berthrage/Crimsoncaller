""" from PPlay.sprite import *
from Player import *

class Warrior:
    def __init__(self, health = 100):
        self.health = health
        self.sprites = []
        self.sprites.append(Sprite("sprites/enemies/warrior1/warrior01.png"))
        self.sprites.append(Sprite("sprites/enemies/warrior1/warrior02.png"))
        self.sprites.append(Sprite("sprites/enemies/warrior1/warrior03.png"))
        self.sprites.append(Sprite("sprites/enemies/warrior1/warrior04.png"))
        self.sprites.append(Sprite("sprites/enemies/warrior1/warrior05.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image.set_position(900, 440)
        self.ready = True
        self.walking = False

    def update_sprite(self):
        if self.health > 0:
            self.atual += 0.05
            x = self.image.x
            if self.atual > len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            x -= 0.5
            self.image.set_position(x,440)
            self.image.draw()
            self.image.update()
        else:
            print(self.health)

    def combat(self):
        if self.image.collided(Player.sprite) and Player.attacking and self.ready:
            self.health -= 25
            GameWindow.window.draw_text('-25', self.image.x, self.image.y, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            self.ready = False
            print('dano')
        else:
            if not Player.attacking:
                self.ready = True """