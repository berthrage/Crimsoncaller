from PPlay.sprite import *
from Player import *
from PPlay.collision import *
from GameWindow import *

class Devotee:
    def __init__(self, health=100):
        self.health = health
        self.sprites = []
        self.sprites.append(Sprite("sprites/enemies/devotee/Devotee-praying_01.gif"))
        self.sprites.append(Sprite("sprites/enemies/devotee/Devotee-praying_02.gif"))
        self.sprites.append(Sprite("sprites/enemies/devotee/Devotee-praying_03.gif"))
        self.sprites.append(Sprite("sprites/enemies/devotee/Devotee-praying_04.gif"))
        self.sprites.append(Sprite("sprites/enemies/devotee/Devotee-praying_05.png"))
        self.sprites.append(Sprite("sprites/enemies/devotee/Devotee-praying_06.gif"))
        self.sprites.append(Sprite("sprites/enemies/devotee/Devotee-praying_07.gif"))
        self.sprites.append(Sprite("sprites/enemies/devotee/Devotee-praying_08.gif"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.ready = True

    def update_sprite(self):        
        self.atual += 0.05
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image.set_position(900,500)
        self.image.draw()
        self.image.update()

    def collision(self):
        if self.image.collided(Player.sprite) and Player.attacking and self.ready:
            self.health -= 25
            GameWindow.window.draw_text('-25', self.image.x, self.image.y, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            self.ready = False
            print('dano')
        else:
            if not Player.attacking:
                self.ready = True