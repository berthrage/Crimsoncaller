import Player
from GameWindow import GameWindow
from Input import *
import Levels
from Player import *
import HUD
import Warrior
import MainMenu
import Devotee
import Cerbero
import Demon
from Enemy import allEnemies

class Game:
    name = "Game"
    windowColor = [15, 34, 41]
    HUD = HUD.HUD()
    timeElapsed = 0
    gameLoops = 0
    frameRate = 0
    currentLevel = Level1area1()
    #currentLevel = Level1area2()
    #currentLevel = Level1area3()
    transitioningLevel = False
    intervalTransitionLevel = 0.05
    transitionLevelTimer = Misc.Timer()
    levelToTransition = Level1area1()
    levelToTransitionPlayerPos = [0, 0]
    level3defeat = 0
    readyToWin = False

    @staticmethod
    def executeGame():


        while True:
            GameWindow.window.set_background_color(Game.windowColor)
            Input.inputHandler()

            Game.currentLevel.spawnLevel()
            Game.handleLevels()
            #Player.spawnJulius()
            Player.controlJulius(Game.currentLevel)
            Game.backtoMainMenu()
            Game.HUD.renderHUD()
            Game.lose()
            Game.win()
            Game.showFrameRate()
            GameWindow.window.update()


    @staticmethod
    def handleLevels():
        if(isinstance(Game.currentLevel, Level1area1)):
            if(Player.sprite.x > GameWindow.window.width - 75):
                Game.transitionLevel(0, 300)
                if(Game.transitionLevelTimer.time >= Game.intervalTransitionLevel - 0.03):
                    Game.levelToTransition = Level1area2()
            elif Player.sprite.x <= 0:
                Player.sprite.x = 5

        elif(isinstance(Game.currentLevel, Level1area2)):
            if(Player.sprite.x < 0):
                Player.sprite.x = 10
                """ Game.transitionLevel(1150, 200, -1280)
                if (Game.transitionLevelTimer.time >= Game.intervalTransitionLevel - 0.03):
                    Game.levelToTransition = Level1area1() """

            elif(Player.sprite.x > GameWindow.window.width - 75):
                Game.transitionLevel(0, 300)
                if(Game.transitionLevelTimer.time >= Game.intervalTransitionLevel - 0.03):
                    Game.levelToTransition = Level1area3()

        elif (isinstance(Game.currentLevel, Level1area3)):
            if Player.sprite.x <= 0:
                Player.sprite.x = 5
            if (not Game.readyToWin) and Player.sprite.x >= GameWindow.window.width - 80:
                Player.sprite.x = GameWindow.window.width - 85
            if Game.readyToWin and Player.sprite.x >= GameWindow.window.width:
                Game.executeWinScreen()

            GameWindow.window.draw_text(f"px: {Player.sprite.x}", GameWindow.window.width/2, 0, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            GameWindow.window.draw_text(f"gw: {GameWindow.window.width - 10}", GameWindow.window.width/2, 100, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            GameWindow.window.draw_text(f"rw: {Game.readyToWin}", GameWindow.window.width/2, 200, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)

    @staticmethod
    def transitionLevel(playerX, playerY, levelX=0):

        Game.transitionLevelTimer.resumeTimer()
        Game.transitionLevelTimer.executeTimer()
        Game.transitioningLevel = True
        if (Game.transitionLevelTimer.time >= Game.intervalTransitionLevel - 0.01):
            Game.currentLevel = Game.levelToTransition
            #Player.sprite.set_position(playerX, playerY)
            Player.sprite.set_position(0, 0)
            Game.currentLevel.tiles.x = levelX
            Game.currentLevel.background.x = levelX / 2

        if (Game.transitionLevelTimer.time >= Game.intervalTransitionLevel):

            Game.transitionLevelTimer.stopTimer()
            Game.transitionLevelTimer.resetTimer()


    @staticmethod
    def backtoMainMenu():
        if(Input.getKeyDown("ESC")):
            #Game.currentLevel.resetLevel()
            Game.resetGame()
            return MainMenu.MainMenu.executeMainMenu()

    @staticmethod
    def resetGame():
        Game.currentLevel = Level1area1()
        Player.sprite.set_position(200, 0)
        Player.health = 100

    @staticmethod
    def showFrameRate():
        if (Game.timeElapsed >= 0.3):
            Game.frameRate = Game.gameLoops / Game.timeElapsed
            Game.timeElapsed = 0
            Game.gameLoops = 0
        elif (Game.timeElapsed < 0.3):

            Game.timeElapsed += GameWindow.window.delta_time()
            Game.gameLoops += 1

        GameWindow.window.draw_text("FPS: " + str(int(Game.frameRate)), 1200, 10, 15, [255, 234, 0], "Arial", True)

    @staticmethod
    def executeLoseScreen():
        loseSprite = Sprite('sprites/menu_old/lose.png')
        while True:
            GameWindow.window.set_background_color(Game.windowColor)
            GameWindow.window.draw_text("DEAD", GameWindow.window.width/2, GameWindow.window.height,
                 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            loseSprite.draw()
            Game.backtoMainMenu()
            GameWindow.window.update()


    @staticmethod
    def lose():
        if Player.health <= 0:
            return Game.executeLoseScreen()
        if not (isinstance(Game.currentLevel, Level1area3)) and (Player.sprite.y >= GameWindow.window.height + Player.sprite.height):
            return Game.executeLoseScreen()

    @staticmethod
    def executeWinScreen():
        winSprite = Sprite('sprites/menu_old/win.png')
        while True:
            GameWindow.window.set_background_color(Game.windowColor)
            GameWindow.window.draw_text("WIN", GameWindow.window.width/2, GameWindow.window.height,
                 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            winSprite.draw()
            Game.backtoMainMenu()
            GameWindow.window.update()

    @staticmethod
    def win():
        mortos = 0
        if (isinstance(Game.currentLevel, Level1area3)):
            for i in Game.currentLevel.enemies:
                if i.health <= 0:
                    mortos += 1
            if mortos >= 4:
                Game.readyToWin = True
            else:
                return