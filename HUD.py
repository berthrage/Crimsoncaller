from GameWindow import *
from Player import Player
from PPlay.sprite import *

class HUD:
    def __init__(self):
        self.blackscreensprite = Sprite("sprites/blackscreen.png")
        self.blackScreenTransitionTimer = Misc.Timer()

    def renderHUD(self):
        from Game import Game
        GameWindow.window.draw_text(str(Player.health), 40, 60, 90, [255, 0, 0], "fonts/AncientModernTales.ttf", False,
                                    False, False)
        GameWindow.window.draw_text("Press I to attack", 40, 180, 30, [255, 0, 0], "fonts/AncientModernTales.ttf", False,
                                    False, False)

        if(Game.transitioningLevel):
            self.blackscreensprite.draw()

            self.blackScreenTransitionTimer.resumeTimer()
            self.blackScreenTransitionTimer.executeTimer()

            if(self.blackScreenTransitionTimer.time >= Game.intervalTransitionLevel + 0.1):
                self.blackScreenTransitionTimer.stopTimer()
                self.blackScreenTransitionTimer.resetTimer()
                Game.transitioningLevel = False