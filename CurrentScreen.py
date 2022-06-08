from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

class Screen:
    name = "screenname"
    windowColor = [0, 0, 0]
    order = 1

class MainMenu:
    name = "Main Menu"
    windowColor = [0, 0, 0]
    order = 0

class Level1(Screen):
    name = "Lunerian Castle"
    windowColor = [15, 34, 41]

class Level2(Screen):
    name = "Lunerian Castle Underground"
    windowColor = [0, 0, 0]
    order = 2