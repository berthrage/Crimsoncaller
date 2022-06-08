from PPlay.sprite import *
from PPlay.gameobject import *
from GameWindow import GameWindow
from Levels import *
from Input import *
import pygame

class Player:
    direction = 2         #2 means right, 1 means left
    standing = True
    still = True
    sprite = Sprite("sprites/player/right/julius-idle1-right.png", 15)
    sprite.set_sequence_time(0, 14, 80, True)
    sprite.set_position(200, 490)

    @staticmethod
    def spawnJulius():
        Player.sprite.draw()
        Player.sprite.update()

        #Julius.setGravity()
        #Julius.sprite.mask.scale((800, 900))

    @staticmethod
    def controlJulius():

        """if(Input.getKeyDown("d")):
            Player.direction = 2
        if(Input.getKeyDown(("a"))):
            Player.direction = 1"""

        if(GameWindow.window.keyboard.key_pressed("d")):
            Player.direction = 2
            Player.still = False
        elif(GameWindow.window.keyboard.key_pressed("a")):
            Player.direction = 1
            Player.still = False
        else:
            Player.still = True

        if(Player.still and Player.standing and Player.direction == 2):
            JuliusAnim.idle1_right = True
            #JuliusAnim.idle1_right = False
        elif(Player.still and Player.standing and Player.direction == 1):
            JuliusAnim.idle1_left = True
            #JuliusAnim.idle1_left = False
        elif(not Player.still and Player.standing and Player.direction == 2):
            JuliusAnim.walk_right = True

        elif(not Player.still and Player.standing and Player.direction == 1):
            JuliusAnim.walk_left = True
            JuliusAnim.timeElapsed += GameWindow.window.delta_time()

        if(not Player.still and Player.direction == 2):
            Player.sprite.x += 200 * GameWindow.window.delta_time()
        elif(not Player.still and Player.direction == 1):
            Player.sprite.x -= 200 * GameWindow.window.delta_time()

        JuliusAnim.setAnim()


    @staticmethod
    def setGravity():
        if(not pygame.sprite.collide_mask(Level1area1.tiles, Player.sprite)):
            Player.sprite.y += 200 * GameWindow.window.delta_time()

class JuliusAnim():
    idle1_right = False
    idle1_right_animChanged = False

    idle1_left = False
    idle1_left_animChanged = False

    walk_right = False
    walk_right_animChanged = False

    walk_left = False
    walk_left_animChanged = False

    timeElapsed = 0

    currentX = 0
    currentY = 0

    @staticmethod
    def changeAnim():
        pass

    @staticmethod
    def setAnim():
        currentX = Player.sprite.x
        currentY = Player.sprite.y

        if(JuliusAnim.idle1_right and not JuliusAnim.idle1_right_animChanged):
            Player.sprite = Sprite("sprites/player/right/julius-idle1-right.png", 15)
            Player.sprite.set_sequence_time(0, 14, 80, True)
            Player.sprite.set_position(currentX, currentY)

            JuliusAnim.idle1_right_animChanged = True
            JuliusAnim.idle1_right = False

            JuliusAnim.idle1_left_animChanged = False
            JuliusAnim.walk_right_animChanged = False
            JuliusAnim.walk_left_animChanged = False

        elif(JuliusAnim.idle1_left and not JuliusAnim.idle1_left_animChanged):
            Player.sprite = Sprite("sprites/player/left/julius-idle1-left.png", 15)
            Player.sprite.set_sequence_time(0, 14, 80, True)
            Player.sprite.set_position(currentX, currentY)

            JuliusAnim.idle1_left_animChanged = True
            JuliusAnim.idle1_left = False

            JuliusAnim.idle1_right_animChanged = False
            JuliusAnim.walk_right_animChanged = False
            JuliusAnim.walk_left_animChanged = False

        elif(JuliusAnim.walk_right and not JuliusAnim.walk_right_animChanged):
            Player.sprite = Sprite("sprites/player/right/julius-walk-right.png", 16)
            Player.sprite.set_sequence_time(0, 15, 40, True)
            Player.sprite.set_position(currentX, currentY)

            JuliusAnim.walk_right_animChanged = True
            JuliusAnim.walk_right = False

            JuliusAnim.idle1_right_animChanged = False
            JuliusAnim.idle1_left_animChanged = False
            JuliusAnim.walk_left_animChanged = False

        elif (JuliusAnim.walk_left and not JuliusAnim.walk_left_animChanged):


            #Player.sprite = Sprite("sprites/player/left/julius-walkstart-left.png", 5)
            #Player.sprite.set_sequence_time(0, 4, 80, False)
            #Player.sprite.set_position(currentX, currentY)

            #if(JuliusAnim.timeElapsed >= 1):
            Player.sprite = Sprite("sprites/player/left/julius-walk-left.png", 16)
            Player.sprite.set_sequence_time(0, 15, 40, True)
            Player.sprite.set_position(currentX, currentY)


            JuliusAnim.walk_left_animChanged = True
            JuliusAnim.walk_left = False

            JuliusAnim.idle1_right_animChanged = False
            JuliusAnim.idle1_left_animChanged = False
            JuliusAnim.walk_right_animChanged = False