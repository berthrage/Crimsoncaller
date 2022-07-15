from Enemy import *
from Animations import AnimatedSprite
from PPlay.sprite import *
from GameWindow import *
from Enemy import allEnemies

class Dragon(Enemy):
    def __init__(self, positionX, positionY, direction='left', health=100):
        super().__init__(positionX, positionY, health)
        self.health = health
        self.speed = 150
        self.damage = 25
        self.direction = direction
        self.detected = False
        self.patrolling = True
        self.walk = False
        self.attack = False
        self.readyToDie = True
        self.sprite = Sprite("sprites/enemies/dragon/walking/1.png")
        self.tick = 1

        self.animatedSprites = []

        self.walkingAnim = AnimatedSprite()
        self.walkingAnim.addSprite("sprites/enemies/dragon/walking", 5)
        self.animatedSprites.append(self.walkingAnim)

        self.attackingAnim = AnimatedSprite()
        self.attackingAnim.addSprite("sprites/enemies/dragon/attacking", 4)
        self.animatedSprites.append(self.attackingAnim)

        self.dyingAnim = AnimatedSprite()
        self.dyingAnim.addSprite("sprites/enemies/dragon/death", 5)
        self.animatedSprites.append(self.dyingAnim)

        self.hurtAnim = AnimatedSprite()
        self.hurtAnim.addSprite("sprites/enemies/dragon/hurt", 2)
        self.animatedSprites.append(self.hurtAnim)

    def patrulhando(self, direction):
        if (self.direction == direction and
            self.patrolling):
            return True
        else:
            return False

    def detectado(self):
        from Player import Player
        if (self.sprite.x - Player.sprite.x <= 250):
            self.detected = True
            self.patrolling = False
            self.walk = True

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

        if not self.detected:
            self.detectado()
            if self.patrulhando('left'):
                print(self.initialPositionX - self.sprite.x)
                if self.initialPositionX - self.sprite.x <= 200:
                    self.sprite.x -= GameWindow.window.delta_time() * self.speed
                else:
                    print('entrou right')
                    self.direction = 'right'
            elif self.patrulhando('right'):
                if self.initialPositionX >= self.sprite.x:
                    self.sprite.x += GameWindow.window.delta_time() * self.speed
                else:
                    self.direction = 'left'

        else:
            if self.andando('left'):
                self.sprite.x -= GameWindow.window.delta_time() * self.speed
                if self.sprite.x <= Player.sprite.x - 25 :
                    self.walk = False
                    self.attack = True
                    self.sprite.x += 25

            elif self.andando('right'):
                self.sprite.x += GameWindow.window.delta_time() * self.speed
                if self.sprite.x >= Player.sprite.x - 100 :
                    self.walk = False
                    self.attack = True
                    self.sprite.x -= 25

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

            if self.andando('left') or (self.patrolling and self.direction == 'left'):
                self.walkingAnim.playAnimationFlipped(self.sprite, 5, self.animatedSprites)
            elif self.andando('right') or (self.patrolling and self.direction == 'right'):
                self.walkingAnim.playAnimation(self.sprite, 5, self.animatedSprites)
            
            elif self.atacando('left'):
                self.attackingAnim.playAnimationFlipped(self.sprite, 4, self.animatedSprites)
            elif self.atacando('right'):
                self.attackingAnim.playAnimation(self.sprite, 4, self.animatedSprites)

            if  self.direction == 'right' and self.sprite.x >= Player.sprite.x + 25:
                self.direction = 'left'

            elif self.direction == 'left' and self.sprite.x <= Player.sprite.x - 25:
                self.direction = 'right'

            GameWindow.window.draw_text(str(f'detectado: {self.detected}'), 20, 170, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(f'direcao: {self.direction}'), 20, 200, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(f'posicao inicial: {self.initialPositionX}'), 20, 260, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(f'posicao atual: {self.sprite.x}'), 20, 290, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(f'patrulhando: {self.patrolling}'), 20, 320, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(f'andando: {self.walk}'), 20, 350, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(f'atacando: {self.attack}'), 20, 380, 30, [255, 255, 255], "Arial")
            self.movController()

        elif self.dying('left') and self.tick >= 0:
            self.dyingAnim.playAnimationFlipped(self.sprite, 5, self.animatedSprites)
            self.tick -= GameWindow.window.delta_time()
            #if self.dyingAnim.currentFrame >= 4:
            #    self.readyToDie = False
        elif self.dying('right') and self.tick >= 0:
            self.dyingAnim.playAnimation(self.sprite, 5, self.animatedSprites)
            self.tick -= GameWindow.window.delta_time()
            #if self.dyingAnim.currentFrame >= 4:
            #    self.readyToDie = False