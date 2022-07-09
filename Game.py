import Player
from GameWindow import GameWindow
from Input import *
import Levels
from Player import *
import Devotee
import Guerreiro
import MainMenu

class Game:
    name = "Game"
    windowColor = [15, 34, 41]

    timeElapsed = 0
    gameLoops = 0
    frameRate = 0
    currentLevel = Level1area1

    #warrior1 = Warrior()


    @staticmethod
    def executeGame():
        devotee1 = Devotee.Devotee()
        devotee2 = Devotee.Devotee()
        guerreiro1 = Guerreiro.Guerreiro()

        while True:
            GameWindow.window.set_background_color(Game.windowColor)
            Input.inputHandler()

            Levels.spawnLevel(Game.currentLevel)
            devotee1.spawnDevotee(100, 465)
            devotee2.spawnDevotee(600, 465)

            #devotee1.move()


            Player.spawnJulius()
            Player.controlJulius(Game.currentLevel)

            """ if Game.warrior1.health > 0:
                Game.warrior1.update_sprite()
                Warrior.combat(Game.warrior1) """

            guerreiro1.update_sprite()


            '''if Game.devotee1.health > 0:
                Game.devotee1.update_sprite()
                Devotee.collision(Game.devotee1)'''

            print(guerreiro1.image.collided_perfect(Player.sprite))

            Game.backtoMainMenu()
            #GameWindow.window.draw_text(str(JuliusAnim.timeElapsed), 20, 20, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(JuliusAnim.idle1_right), 20, 60, 30, [255, 255, 255], "Arial")
           # GameWindow.window.draw_text(str(JuliusAnim.idle1_left), 20, 90, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(Level1area1.reachedLimitLeft), 20, 90, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(Level1area1.reachedLimitRight), 20, 110, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(Level1area1.tiles.x), 20, 130, 30, [255, 255, 255], "Arial")

            #GameWindow.window.draw_text(str(Player.jumping), 20, 90, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(Player.jumpingTimer.time), 20, 110, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(Player.jumpSpeed), 20, 130, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(Player.jumpSpeedDivision), 20, 150, 30, [255, 255, 255], "Arial")


            GameWindow.window.draw_text(str(Player.health), 40, 60, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            GameWindow.window.draw_text(f"falling: {Player.falling}", 20, 90, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(f"grounded: {Player.grounded}", 20, 110, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(Player.currentSpeed), 20, 130, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(devotee1.posSet), 20, 150, 30, [255, 255, 255], "Arial")

            #GameWindow.window.draw_text(str(Player.health), 40, 60, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            #GameWindow.window.draw_text(str(Game.devotee1.ready), 40, 60, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False, False, False)
            #GameWindow.window.draw_text(str(Player.falling), 20, 90, 30, [255, 255, 255], "Arial")
            #GameWindow.window.draw_text(str(Player.grounded), 20, 110, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(Level1area1.tiles.collided_perfect(Player.sprite)), 20, 170, 30, [255, 255, 255], "Arial")
            GameWindow.window.draw_text(f"groundLevelY: {Player.groundLevelY}", 20, 190, 30,
                                        [255, 255, 255], "Arial")
            GameWindow.window.draw_text(f"groundLevelX: {Player.groundLevelX}", 20, 210, 30,
                                        [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(Player.sprite.rect.bottom), 20, 230, 30,
                                        [255, 255, 255], "Arial")
            GameWindow.window.draw_text(str(Player.collidedGround), 20, 250, 30,
                                        [255, 255, 255], "Arial")
            GameWindow.window.draw_text(f"freefalling: {Player.freeFalling}", 20, 270, 30,
                                        [255, 255, 255], "Arial")
            GameWindow.window.draw_text(f"Player.x: {Player.sprite.x}", 20, 290, 30,
                                        [255, 255, 255], "Arial")
            GameWindow.window.draw_text(f"Player.y: {Player.sprite.y}", 20, 310, 30,
                                        [255, 255, 255], "Arial")

            #GameWindow.window.draw_text(str(Player.sprite.mask.get_size()), 20, 130, 30, [255, 255, 255], "Arial")
            #Player.sprite.mask = pygame.mask.from_surface(Player.sprite.image, 127)

            """mask1 = pygame.mask.from_surface(Player.sprite.image)
            mask2 = pygame.mask.from_surface(Level1area1.tiles.image)

            olist = mask1.outline()
            olist2 = mask2.outline()

            pygame.draw.lines(Player.sprite.image, (255,0,0), True, olist)
            pygame.draw.lines(Level1area1.tiles.image, (255, 255, 255), True, olist2)"""

            #outlinePlayer = Player.sprite.mask.outline()
            #pygame.draw.lines(Player.sprite.image, (255, 0, 0), True, outlinePlayer)




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

