import Player
from Enemy import Enemy
from PPlay.sprite import *
from Warrior import Warrior
from Demon import Demon
from Devotee import Devotee
from Dragon import Dragon
import Player

class Level:
    def __init__(self, background=Sprite("sprites/maps/1-1/1-1-background.png"), tiles=Sprite("sprites/maps/1-1/1-1-tiles.png")):
        self.background = Sprite("sprites/maps/1-1/1-1-background.png")
        self.tiles = Sprite("sprites/maps/1-1/1-1-tiles.png")

        self.scrollingLimit = 550
        self.reachedLimitRight = False
        self.reachedLimitLeft = False
        self.enemies = []
        self.enemies.append(Enemy(400, 200))
        self.enemies.clear()
        self.spawnedEnemies = False

    def spawnLevel(self):
        self.background.draw()
        self.tiles.draw()

        if (not self.spawnedEnemies):
            self.createEnemies()
            self.spawnedEnemies = True

        for enemy in self.enemies:
            enemy.spawn()
            enemy.animationController()

    def resetLevel(self):
        self.enemies.clear()
        self.spawnedEnemies = False

    def createEnemies(self):
        pass


class Level1area1(Level):
    def __init__(self):
        super().__init__()

    def createEnemies(self):
        from Game import Game
        self.enemies.append(Devotee(450 + Game.currentLevel.tiles.x, 210))
        #self.enemies.append(Demon(900 + Game.currentLevel.tiles.x, 465))
        self.enemies.append(Warrior(1900 + Game.currentLevel.tiles.x, 325))


        #self.enemies.append(Warrior(700, 325))
        #self.enemies.append(Devotee(800 + Game.currentLevel.tiles.x, 465))
        self.enemies.append(Dragon(1900 + Game.currentLevel.tiles.x, 465))

class Level1area2(Level):
    def __init__(self):
        super().__init__()
        self.background = Sprite("sprites/maps/1-1/1-1-background.png")
        self.tiles = Sprite("sprites/maps/1-2/1-2-tiles.png")

    def createEnemies(self):
        from Game import Game
        self.enemies.append(Warrior(2000 + Game.currentLevel.tiles.x, 325))
        self.enemies.append(Dragon(3000 + Game.currentLevel.tiles.x, 460))
        self.enemies.append(Devotee(280, 150))
        self.enemies.append(Demon(1200, 460))
        self.enemies.append(Devotee(1800, 50))
        self.enemies.append(Dragon(450, 460))

class Level1area3(Level):
    def __init__(self):
        super().__init__()
        self.background = Sprite("sprites/maps/1-3/1-3-background.png")
        self.tiles = Sprite("sprites/maps/1-3/1-3-tiles.png")


    def createEnemies(self):
        from Game import Game
        self.enemies.append(Demon(350, 470))
        self.enemies.append(Dragon(800, 470))
        self.enemies.append(Demon(1200, 470))
        self.enemies.append(Demon(1800, 470))
        