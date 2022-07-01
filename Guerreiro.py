import GameWindow
from PPlay.sprite import *
from Player import *
from Enemy import *

class Guerreiro(Enemy):
    def __init__(self, health = 100):
        super().__init__(health)
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

        self.ready = True
        self.ready2 = True

    def update_sprite(self):

        self.showHealthGuerreiro()
        self.moveAccordingLevelScrollingGuerreiro()
        self.combat()
        self.kill()


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
                if self.image.x <= Player.sprite.x + Player.sprite.width:
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
                if not (self.image.x <= Player.sprite.x + Player.sprite.width):
                    self.walking = True
                    self.attacking = False

    def showHealthGuerreiro(self):


        if (self.mostrarHealth):
            self.mostrarHealthTimer.resumeTimer()
            self.mostrarHealthTimer.executeTimer()


            if (self.show):
                GameWindow.window.draw_text('-10', self.image.x, self.image.y - 50, 60, [255, 0, 0],
                                            "fonts/AncientModernTales.ttf", False, False, False)


            if(self.mostrarHealthTimer.time > self.step):
                if(self.show):
                    self.show = False
                else:
                    self.show = True
                self.step += self.increment



            if (self.mostrarHealthTimer.time >= self.interval):
                self.mostrarHealth = False
                self.step = self.increment
                self.mostrarHealthTimer.stopTimer()
                self.mostrarHealthTimer.resetTimer()

    def moveAccordingLevelScrollingGuerreiro(self):
        if (Pl.Player.direction == 2):
            if (Pl.Player.sprite.x > self.level.scrollingLimit and not Pl.Player.still and not self.level.reachedLimitRight):
                self.image.x -= Pl.Player.currentSpeed * GameWindow.window.delta_time()
        elif (Pl.Player.direction == 1):
            if (Pl.Player.sprite.x < self.level.scrollingLimit and not Pl.Player.still and not self.level.reachedLimitLeft):
                self.image.x += Pl.Player.currentSpeed * GameWindow.window.delta_time()

    def combat(self):
        if self.image.collided_perfect(Player.sprite) and Player.attacking and self.ready:
            self.health -= 10
            self.mostrarHealth = True
            self.ready = False
        else:
            if not Player.attacking:
                self.ready = True
        
        if self.attacking and self.image.collided_perfect(Player.sprite) and self.ready2:
            Player.health -= 25
            self.ready2 = False

        elif not self.attacking:
            self.ready2 = True