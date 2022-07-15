from GameWindow import *
from Misc import *
from Input import *
from PPlay.sprite import *
from MenuSprites import MenuSprites
from PPlay.window import Window
import Game

# executes in game loop

class MainMenu:
    name = "MainMenu"
    windowColor = [0, 0, 0]

    isSelected = "NewGame"

    logoPosition = {'x': GameWindow.window.width / 2 - MenuSprites.logo.width / 2, 'y': GameWindow.window.height / 2 - MenuSprites.logo.height / 2 - 50}
    newgamePosition = {'x': GameWindow.window.width / 2 - MenuSprites.newgame_text.width / 2, 'y': logoPosition['y'] + 200}
    exitPosition = {'x': GameWindow.window.width / 2 - MenuSprites.options_text.width / 2, 'y': logoPosition['y'] + 230}
    #exitPosition = {'x': GameWindow.window.width / 2 - MenuSprites.exit_text.width / 2, 'y': logoPosition['y'] + 260}

    @staticmethod
    def executeMainMenu():
        while True:
            Misc.menuSelected = MainMenu.name
            Misc.inMenu = True
            GameWindow.window.set_background_color(MainMenu.windowColor)
            Input.inputHandler()

            #GameWindow.window.draw_text(str(Input.keyPressed["w"]), 20, 20, 30, [255, 255, 255], "Arial")
            MenuSprites.logo.set_position(MainMenu.logoPosition['x'], MainMenu.logoPosition['y'])
            MenuSprites.newgame_text.set_position(MainMenu.newgamePosition['x'], MainMenu.newgamePosition['y'])
            #MenuSprites.options_text.set_position(MainMenu.optionsPosition['x'], MainMenu.optionsPosition['y'])
            MenuSprites.exit_text.set_position(MainMenu.exitPosition['x'], MainMenu.exitPosition['y'])

            MenuSprites.selection_main.draw()
            MenuSprites.newgame_text.draw()
            #MenuSprites.options_text.draw()
            MenuSprites.exit_text.draw()
            MenuSprites.logo.draw()

            if(MainMenu.isSelected == "NewGame"):
                MenuSprites.selection_main.set_position(MainMenu.newgamePosition['x'], MainMenu.newgamePosition['y'])

            #elif(MainMenu.isSelected == "Options"):
             #   MenuSprites.selection_main.set_position(MainMenu.optionsPosition['x'], MainMenu.optionsPosition['y'])

            elif(MainMenu.isSelected == "Exit"):
                MenuSprites.selection_main.set_position(MainMenu.exitPosition['x'], MainMenu.exitPosition['y'])

            MainMenu.Logic()
            """if(MainMenu.isSelected == "NewGame"):
                if (GameWindow.keyboard.key_pressed("UP") or GameWindow.keyboard.key_pressed("DOWN")):
                    MainMenu.isSelected = "Options"
                    menu.spriteChanged = False
            elif(MainMenu.isSelected == "Options"):
                if (GameWindow.keyboard.key_pressed("UP") or GameWindow.keyboard.key_pressed("DOWN")):
                    MainMenu.isSelected = "NewGame"
                    menu.spriteChanged = False"""

            #GameWindow.gameWindow.draw_text(menu.isSelected, 20, 20, 30, [255, 255, 255], "Arial")



            GameWindow.window.update()

    @staticmethod
    def Logic():
        if(MainMenu.isSelected == "NewGame"):
            if(Input.getKeyDown("w") or Input.getKeyDown("UP")):
                MainMenu.isSelected = "Exit"
            elif(Input.getKeyDown("s") or Input.getKeyDown("DOWN")):
                MainMenu.isSelected = "Exit"
            elif(Input.getKeyDown("e") or Input.getKeyDown("SPACE") or Input.getMouseButtonDown(1)):
                return Game.Game.executeGame()

        elif(MainMenu.isSelected == "Exit"):
            if (Input.getKeyDown("w") or Input.getKeyDown("UP")):
                MainMenu.isSelected = "NewGame"
            elif (Input.getKeyDown("s") or Input.getKeyDown("DOWN")):
                MainMenu.isSelected = "NewGame"
            elif (Input.getKeyDown("e") or Input.getKeyDown("SPACE") or Input.getMouseButtonDown(1)):
                GameWindow.window.clear()
                GameWindow.window.close()

        if(GameWindow.mouse.is_over_object(MenuSprites.newgame_text)):
            MainMenu.isSelected = "NewGame"
        elif (GameWindow.mouse.is_over_object(MenuSprites.exit_text)):
            MainMenu.isSelected = "Exit"
        """ elif(GameWindow.mouse.is_over_object(MenuSprites.options_text)):
            MainMenu.isSelected = "Options" """

        if(Input.getKeyDown("ESC")):
            GameWindow.window.clear()
            GameWindow.window.close()

        """elif(MainMenu.isSelected == "Options"):
            if (GameWindow.keyboard.key_pressed("UP") or GameWindow.keyboard.key_pressed("DOWN")):
                MainMenu.isSelected = "NewGame"""""

        """ elif(MainMenu.isSelected == "Options"):
            if (Input.getKeyDown("w") or Input.getKeyDown("UP")):
                MainMenu.isSelected = "NewGame"
            elif (Input.getKeyDown("s") or Input.getKeyDown("DOWN")):
                MainMenu.isSelected = "Exit"
            elif (Input.getKeyDown("e") or Input.getKeyDown("SPACE") or Input.getMouseButtonDown(1)):
                pass """



