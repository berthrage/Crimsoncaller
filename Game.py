from GameWindow import GameWindow
from Input import *
from Levels import *
from Player import *
import MainMenu

class Game:
    name = "Game"
    windowColor = [15, 34, 41]

    timeElapsed = 0
    gameLoops = 0
    frameRate = 0

    @staticmethod
    def executeGame():
        while True:
            GameWindow.window.set_background_color(Game.windowColor)


            Levels.spawnLevel(Level1area1)
            Player.spawnJulius()
            Player.controlJulius()
            Game.backtoMainMenu()
            #GameWindow.window.draw_text(str(JuliusAnim.timeElapsed), 20, 20, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(JuliusAnim.idle1_right), 20, 60, 30, [255, 255, 255], "Arial")
           # GameWindow.window.draw_text(str(JuliusAnim.idle1_left), 20, 90, 30, [255, 255, 255], "Arial")
            Game.showFrameRate()
            GameWindow.window.update()


    @staticmethod
    def backtoMainMenu():
        if(Input.getKeyDown("ESC")):
            return MainMenu.MainMenu.executeMainMenu()

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

