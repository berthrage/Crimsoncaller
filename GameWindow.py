#Leandro Bertoldo RA: 219031092
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from CurrentScreen import *
from Misc import  *



class GameWindow:
    window = Window(1280, 720)
    keyboard = window.get_keyboard()
    mouse = window.get_mouse()


GameWindow.window.set_title("Crimsoncaller")
#GameWindow.window.set_fullscreen()

