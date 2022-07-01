from PPlay.sprite import *
from Player import *

class Guerreiro:
    def __init__(self, health = 100):
        self.health = health

        self.sprites_off = []
        self.sprites_off.append(Sprite("sprites/enemies/warrior/unsheathing/warrior01.png"))
        self.sprites_off.append(Sprite("sprites/enemies/warrior/unsheathing/warrior02.png"))
        self.sprites_off.append(Sprite("sprites/enemies/warrior/unsheathing/warrior03.png"))
        self.sprites_off.append(Sprite("sprites/enemies/warrior/unsheathing/warrior04.png"))
        self.sprites_off.append(Sprite("sprites/enemies/warrior/unsheathing/warrior05.png"))
        
        self.sprites_walking = []
        self.sprites_walking.append(Sprite("sprites/enemies/warrior/walking/warrior01.png"))
        self.sprites_walking.append(Sprite("sprites/enemies/warrior/walking/warrior02.png"))
        self.sprites_walking.append(Sprite("sprites/enemies/warrior/walking/warrior03.png"))
        self.sprites_walking.append(Sprite("sprites/enemies/warrior/walking/warrior04.png"))
        self.sprites_walking.append(Sprite("sprites/enemies/warrior/walking/warrior05.png"))

        self.sprites_attacking = []
        self.sprites_attacking.append(Sprite("sprites/enemies/warrior/attacking/warrior01.png"))
        self.sprites_attacking.append(Sprite("sprites/enemies/warrior/attacking/warrior02.png"))
        self.sprites_attacking.append(Sprite("sprites/enemies/warrior/attacking/warrior03.png"))
        self.sprites_attacking.append(Sprite("sprites/enemies/warrior/attacking/warrior04.png"))
        self.sprites_attacking.append(Sprite("sprites/enemies/warrior/attacking/warrior05.png"))

        self.atual = 0
        self.image = self.sprites_off[0]
        self.image.set_position(900, 450)
        self.off = False
        self.unsheathing = True
        self.walking = False
        self.attacking = False
        self.ready = True
        self.ready2 = True

    def update_sprite(self):
        if self.health > 0:
            if self.off:
                self.image.draw()
                self.image.update()

            elif self.unsheathing:
                self.atual += 0.05        
                if self.atual >= len(self.sprites_off):
                    self.atual = 4
                    self.unsheathing = False
                    self.walking = True
                self.image = self.sprites_off[int(self.atual)]
                self.image.set_position(900, 450)


                self.image.draw()
                self.image.update()

            elif self.walking:
                self.atual += 0.05
                x = self.image.x
                if self.atual >= len(self.sprites_walking):
                    self.atual = 0
                self.image = self.sprites_walking[int(self.atual)]
                x -= 1
                self.image.set_position(x,440)
                self.image.draw()
                self.image.update()
                if self.image.x <= Player.sprite.x + Player.sprite.width + 50:
                    self.walking = False
                    self.attacking = True

            elif self.attacking:
                self.atual += 0.05
                x = self.image.x
                if self.atual >= len(self.sprites_attacking):
                    self.atual = 0
                self.image = self.sprites_attacking[int(self.atual)]
                self.image.set_position(x,420)
                self.image.draw()
                self.image.update()
                if not (self.image.x <= Player.sprite.x + Player.sprite.width + 50):
                    self.walking = True
                    self.attacking = False


    def combat(self):
        if self.image.collided(Player.sprite) and Player.attacking and self.ready:
            self.health -= 50
            GameWindow.window.draw_text('-50', self.image.x, self.image.y, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            self.ready = False
        else:
            if not Player.attacking:
                self.ready = True
        
        if self.attacking and self.image.collided(Player.sprite):
            Player.health -= 25