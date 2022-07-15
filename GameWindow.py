#Leandro Bertoldo RA: 219031092
#Hendel Fonseca RA: 221031107
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from CurrentScreen import *
from Misc import  *



class GameWindow:

    window = Window(1280, 720)
    keyboard = window.get_keyboard()
    mouse = window.get_mouse()
    sound = Sound("music/test.ogg")
    sound.set_volume(10)
    sound.play()

GameWindow.window.set_title("Crimsoncaller")
GameWindow.window.set_fullscreen()

