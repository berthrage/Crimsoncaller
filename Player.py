from Animations import AnimatedSprite
import Levels
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.collision import *
from GameWindow import GameWindow
from Levels import *
from Input import *
import pygame
import Game
from Enemy import Enemy, allEnemies

class Player:
    health = 100
    direction = 2         #2 means right, 1 means left
    standing = True
    still = True
    sliding = False
    slidingTimer = Misc.Timer()
    jumping = False
    freeFalling = False
    freeFallingTimer = Misc.Timer()
    falling = False
    grounded = False
    jumpingTimer = Misc.Timer()
    attacking = False
    attack = False
    attackOffCooldown = True
    attackingTimer = Misc.Timer()
    attackCooldownTimer = Misc.Timer()
    groundLevelY = 0
    groundLevelX = 0
    collidedGround = False
    collidedWall = False

    sprite = Sprite("sprites/player/right/julius-idle/1.png")
    sprite.set_sequence_time(0, 14, 80, True)
    levelGroundFloor = 465
    sprite.set_position(200, 0)
    #sprite.set_position(1000, 0)
    walkSpeed = 250
    dashSpeed = 600
    jumpSpeed = 1200
    jumpSpeedDivision = 5000
    fallSpeed = 800
    tempDashSpeed = dashSpeed
    tempJumpSpeed = jumpSpeed
    tempJumpSpeedDivision = jumpSpeedDivision
    tempFallSpeed = fallSpeed
    currentSpeed = 0


    @staticmethod
    def spawnJulius(): pass
        #Player.sprite.draw()
        #Player.sprite.update()

        #Julius.setGravity()
        #Julius.sprite.mask.scale((800, 900))

    @staticmethod
    def controlJulius(Level):

        if(Input.getKeyDown("d")):
            Player.direction = 2
        if(Input.getKeyDown("a")):
            Player.direction = 1

        if((GameWindow.window.keyboard.key_pressed("d") or GameWindow.window.keyboard.key_pressed("a")) and Player.standing or Player.sliding):
            #Player.direction = 2
            Player.still = False
        else:
            Player.still = True

        if(Player.attacking and Player.grounded):
            Player.still = True

        if(GameWindow.window.keyboard.key_pressed("s") and not Player.jumping and not Player.falling):
            Player.standing = False
        elif(not GameWindow.window.keyboard.key_pressed("s") and not Player.sliding):
            Player.standing = True



        if(not Player.standing and not Player.jumping and not Player.freeFalling and not Player.falling and Input.getKeyDown("SPACE")):
            Player.sliding = True

        if(Player.sliding):
            Player.slidingTimer.resumeTimer()
            Player.slidingTimer.executeTimer()

            if(Player.slidingTimer.time >= 0.8):
                Player.sliding = False
                Player.slidingTimer.stopTimer()
                Player.slidingTimer.resetTimer()


        if(not Player.attacking and not Player.freeFalling and not Player.falling and Input.getKeyDown("SPACE")):
            Player.jumping = True
        if (Player.jumping):
            Player.jumpingTimer.resumeTimer()
            Player.jumpingTimer.executeTimer()

            if(GameWindow.keyboard.key_pressed("SPACE") and Player.jumpSpeedDivision > 1400):
                Player.jumpSpeedDivision -= 10000 * GameWindow.window.delta_time()
                Player.jumpSpeed += 1100 * GameWindow.window.delta_time()

            if (not Player.jumpSpeed > 0):
                Player.jumping = False
                Player.jumpingTimer.stopTimer()
                Player.jumpingTimer.resetTimer()

        if(Player.standing and Input.getKeyDown("i") and Player.attackOffCooldown):
            Player.attacking = True
            Player.attackOffCooldown = False
        if(Player.attacking):
            Player.attackingTimer.resumeTimer()
            Player.attackingTimer.executeTimer()

            if(Player.attackingTimer.time >= 0.4):
                Player.attacking = False
                JuliusAnim.lockAttackAnim = False
                Player.attackingTimer.stopTimer()
                Player.attackingTimer.resetTimer()

        if(not Player.attackOffCooldown):
            Player.attackCooldownTimer.resumeTimer()
            Player.attackCooldownTimer.executeTimer()

            if(Player.attackCooldownTimer.time >= 0.5):
                Player.attackOffCooldown = True
                Player.attackCooldownTimer.stopTimer()
                Player.attackCooldownTimer.resetTimer()

        #JuliusAnim.setAnims()
        JuliusAnim.animationController()

        @staticmethod
        def verifyColissionEnemies(direction):
            for enemy in allEnemies:
                if direction == 1 and Player.sprite.x <= enemy.sprite.x and not(Player.sprite.y + Player.sprite.height <= enemy.sprite.y):
                    return False
                if direction == 2 and Player.sprite.x >= enemy.sprite.x and not(Player.sprite.y + Player.sprite.height <= enemy.sprite.y):
                    return False
            return True
        """ @staticmethod
        def verifyColissionEnemies(direction):
            for enemy in allEnemies:
                if Player.sprite.collided_perfect(enemy.sprite):
                    return False """

        
        ## WALKING
        if(not Player.still and Player.direction == 2 and Player.standing and not Player.collidedWall): #and verifyColissionEnemies(Player.direction)):
            if(Player.sprite.x < Level.scrollingLimit + 1 or Level.reachedLimitRight):
                Player.sprite.x += Player.walkSpeed * GameWindow.window.delta_time()



                #if (Player.sprite.collided_perfect(Level1area1.tiles)):
                    #Player.groundLevelX += Player.walkSpeed * GameWindow.window.delta_time()


        elif(not Player.still and Player.direction == 1 and Player.standing and not Player.collidedWall): #and verifyColissionEnemies(Player.direction)):
            if(Player.sprite.x > Level.scrollingLimit - 1 or Level.reachedLimitLeft):
                Player.sprite.x -= Player.walkSpeed * GameWindow.window.delta_time()

                #if (Player.sprite.collided_perfect(Level1area1.tiles)):
                    #Player.groundLevelX -= Player.walkSpeed * GameWindow.window.delta_time()



        if(Player.sliding and Player.direction == 2):
            if (Player.sprite.x < Level.scrollingLimit or Level.reachedLimitRight):
                Player.sprite.x += Player.dashSpeed * GameWindow.window.delta_time()

                #Player.currentSpeed = Player.dashSpeed


        elif(Player.sliding and Player.direction == 1):
            if (Player.sprite.x > Level.scrollingLimit or Level.reachedLimitLeft):
                Player.sprite.x -= Player.dashSpeed * GameWindow.window.delta_time()


        elif(not Player.sliding):
            Player.dashSpeed = Player.tempDashSpeed

        if(Player.jumping):
            Player.sprite.y -= Player.jumpSpeed * GameWindow.window.delta_time()
            if(Player.jumpSpeed > 0):
                Player.jumpSpeed -= (Player.jumpSpeedDivision * GameWindow.window.delta_time())
        else:
            Player.jumpSpeed = Player.tempJumpSpeed
            Player.jumpSpeedDivision = Player.tempJumpSpeedDivision


        if(not Player.still and not Player.sliding):
            Player.currentSpeed = Player.walkSpeed
        elif(not Player.still and Player.sliding):
            Player.currentSpeed = Player.dashSpeed
            if(Player.dashSpeed > 0):
                Player.dashSpeed -= 1000 * GameWindow.window.delta_time()


        Player.scrollLevel(Game.Game.currentLevel)
        Player.setGravity()
        Player.setCollision()

    @staticmethod
    def setCollision():
                            ## COLISAO COM AS PAREDES: ainda ta mt cru
        #if (Player.groundLevelX >= 0.03):
            #Player.sprite.x -= 1000 * GameWindow.window.delta_time()
        #if (Player.groundLevelX <= - 6):
            #Player.sprite.x += 2000 * GameWindow.window.delta_time()

        if(Player.groundLevelX >= 0.03 or Player.groundLevelX < -0.03):
            Player.collidedWall = True
        else:
            Player.collidedWall = False

        if (not Player.still and Player.direction == 2 and Player.sprite.collided_perfect(Game.Game.currentLevel.tiles) and Player.groundLevelX < 0.03):
                Player.groundLevelX += 1 * GameWindow.window.delta_time()
        if (not Player.still and Player.direction == 1 and Player.sprite.collided_perfect(Game.Game.currentLevel.tiles) and Player.groundLevelX > -0.03):
                    Player.groundLevelX -= 1 * GameWindow.window.delta_time()

        if (not Player.sprite.collided_perfect(Game.Game.currentLevel.tiles)):
            Player.groundLevelX = 0

                            ## COLISAO COM O CHAO: funciona ok
        if ((not Player.still and Player.grounded and Player.sprite.collided_perfect(
                Game.Game.currentLevel.tiles) and Player.groundLevelY < 0.01 and not Player.collidedWall)):
            Player.sprite.y -= 500 * GameWindow.window.delta_time()
            Player.groundLevelY += 1 * GameWindow.window.delta_time()

        else:
            Player.groundLevelY = 0

    @staticmethod
    def setGravity():
        #groupTiles = pygame.sprite.Group()
        #groupTiles.add(Levels.Level1area1.tiles)
        #if(not pygame.sprite.collide_mask(Levels.Level1area1.tiles, Player.sprite)):
        #Player.sprite.y < Player.levelGroundFloor and not Player.jumping

        if(Player.falling):
            Player.freeFallingTimer.resumeTimer()
            Player.freeFallingTimer.executeTimer()

            if(Player.freeFallingTimer.time >= 0.1):
                Player.freeFalling = True

                Player.freeFallingTimer.stopTimer()
                Player.freeFallingTimer.resetTimer()
        else:
            Player.freeFalling = False

            Player.freeFallingTimer.stopTimer()
            Player.freeFallingTimer.resetTimer()


        if ((not Game.Game.currentLevel.tiles.collided_perfect(
                Player.sprite) and not Player.jumping) or Player.groundLevelY > 0.1):
            Player.sprite.y += Player.fallSpeed * GameWindow.window.delta_time()
            Player.fallSpeed += 200 * GameWindow.window.delta_time()

            Player.falling = True
        else:
            Player.fallSpeed = Player.tempFallSpeed
            Player.falling = False

        if ((Player.falling and Player.freeFalling) or Player.jumping):
            Player.grounded = False
        else:
            Player.grounded = True

        """if(not Player.still and Player.grounded and Player.sprite.collided_perfect(Level1area1.tiles)):
            Player.groundLevelX += Player.walkSpeed * GameWindow.window.delta_time()
        else:
            Player.groundLevelX = 0"""

        """if(Player.sprite.rect.bottom >= Level1area1.tiles.rect.top):
            Player.collidedGround = True
        else:
            Player.collidedGround = False"""

    @staticmethod
    def scrollLevel(Level):
        if (Level.tiles.x >= 0):
            Level.reachedLimitLeft = True
        else:
            Level.reachedLimitLeft = False

        if (Level.tiles.x <= -Level.tiles.width / 2):
            Level.reachedLimitRight = True
        else:
            Level.reachedLimitRight = False

        if (Player.direction == 2):
            if (Player.sprite.x > Level.scrollingLimit and not Player.still and not Player.collidedWall and not Level.reachedLimitRight):
                Level.tiles.x -= Player.currentSpeed * GameWindow.window.delta_time()
                Level.background.x -= (Player.currentSpeed / 2) * GameWindow.window.delta_time()
        elif (Player.direction == 1):
            if (Player.sprite.x < Level.scrollingLimit and not Player.still and not Player.collidedWall and not Level.reachedLimitLeft):
                Level.tiles.x += Player.currentSpeed * GameWindow.window.delta_time()
                Level.background.x += (Player.currentSpeed / 2) * GameWindow.window.delta_time()

class JuliusAnim():

    animatedSprites = []

    idleAnim = AnimatedSprite()
    idleAnim.addSprite("sprites/player/right/julius-idle", 15)
    animatedSprites.append(idleAnim)

    walkAnimation = AnimatedSprite()
    walkAnimation.addSprite("sprites/player/right/julius-walk", 16)
    animatedSprites.append(walkAnimation)

    duckAnim = AnimatedSprite()
    duckAnim.addSprite("sprites/player/right/julius-duck", 8)
    animatedSprites.append(duckAnim)

    slideAnim = AnimatedSprite()
    slideAnim.addSprite("sprites/player/right/julius-slide", 11)
    animatedSprites.append(slideAnim)

    fallAnim = AnimatedSprite()
    fallAnim.addSprite("sprites/player/right/julius-fall", 10)
    animatedSprites.append(fallAnim)

    jumpAnim = AnimatedSprite()
    jumpAnim.addSprite("sprites/player/right/julius-jump", 2)
    animatedSprites.append(jumpAnim)

    jumpStillAnim = AnimatedSprite()
    jumpStillAnim.addSprite("sprites/player/right/julius-jumpstill", 2)
    animatedSprites.append(jumpStillAnim)

    attackAnim = AnimatedSprite()
    attackAnim.addSprite("sprites/player/right/julius-attack", 7)
    animatedSprites.append(attackAnim)

    attackAirAnim = AnimatedSprite()
    attackAirAnim.addSprite("sprites/player/right/julius-attackair", 7)
    animatedSprites.append(attackAirAnim)


    lockAttackAnim = False

    @staticmethod
    def idling(direction):
        if (Player.still and
                Player.standing and
                not Player.jumping and
                not Player.freeFalling and
                not Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False

    @staticmethod
    def walking(direction):
        if (not Player.still and
                Player.standing and
                not Player.jumping and
                not Player.freeFalling and
                not Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False

    @staticmethod
    def ducking(direction):
        if (not Player.standing and
                not Player.sliding and
                not Player.jumping and
                not Player.freeFalling and
                not Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False

    @staticmethod
    def sliding(direction):
        if (not Player.standing and
                Player.sliding and
                not Player.jumping and
                not Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False

    @staticmethod
    def jumpingStill(direction):
        if (Player.standing and
                Player.still and
                not Player.sliding and
                Player.jumping and
                not Player.falling and
                not Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False

    @staticmethod
    def jumpingMoving(direction):
        if (Player.standing and
                not Player.still and
                not Player.sliding and
                Player.jumping and
                not Player.freeFalling and
                not Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False

    @staticmethod
    def falling(direction):
        if (Player.standing and
                not Player.sliding and
                not Player.jumping and
                Player.freeFalling and
                not Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False

    @staticmethod
    def attackingGround(direction):
        if (Player.standing and
                not Player.sliding and
                Player.grounded and
                Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False

    @staticmethod
    def attackingAir(direction):
        if (Player.standing and
                not Player.sliding and
                not Player.grounded and
                Player.attacking and
                Player.direction == direction):
            return True
        else:
            return False



    @staticmethod
    def animationController():

        if (JuliusAnim.idling(2)):
            JuliusAnim.idleAnim.playAnimation(Player.sprite, 15, JuliusAnim.animatedSprites)

            # JuliusAnim.idle1_right = False
        elif (JuliusAnim.idling(1)):
            JuliusAnim.idleAnim.playAnimationFlipped(Player.sprite, 15, JuliusAnim.animatedSprites)

            # JuliusAnim.idle1_left = False
        elif (JuliusAnim.walking(2)):
            JuliusAnim.walkAnimation.playAnimation(Player.sprite, 20, JuliusAnim.animatedSprites)

        elif (JuliusAnim.walking(1)):
            JuliusAnim.walkAnimation.playAnimationFlipped(Player.sprite, 20, JuliusAnim.animatedSprites)

        elif (JuliusAnim.ducking(2)):
            JuliusAnim.duckAnim.playAnimation(Player.sprite, 14, JuliusAnim.animatedSprites, False)

        elif (JuliusAnim.ducking(1)):
            JuliusAnim.duckAnim.playAnimationFlipped(Player.sprite, 14, JuliusAnim.animatedSprites, False)

        elif (JuliusAnim.sliding(2)):
            JuliusAnim.slideAnim.playAnimation(Player.sprite, 24, JuliusAnim.animatedSprites, False)

        elif (JuliusAnim.sliding(1)):
            JuliusAnim.slideAnim.playAnimationFlipped(Player.sprite, 24, JuliusAnim.animatedSprites, False)

        elif (JuliusAnim.jumpingStill(2)):
            JuliusAnim.jumpStillAnim.playAnimation(Player.sprite, 20, JuliusAnim.animatedSprites)

        elif (JuliusAnim.jumpingStill(1)):
            JuliusAnim.jumpStillAnim.playAnimationFlipped(Player.sprite, 20, JuliusAnim.animatedSprites)

        elif (JuliusAnim.jumpingMoving(2)):
            JuliusAnim.jumpAnim.playAnimation(Player.sprite, 20, JuliusAnim.animatedSprites)

        elif (JuliusAnim.jumpingMoving(1)):
            JuliusAnim.jumpAnim.playAnimationFlipped(Player.sprite, 20, JuliusAnim.animatedSprites)

        elif (JuliusAnim.falling(2)):
            JuliusAnim.fallAnim.playAnimation(Player.sprite, 20, JuliusAnim.animatedSprites)

        elif (JuliusAnim.falling(1)):
            JuliusAnim.fallAnim.playAnimationFlipped(Player.sprite, 20, JuliusAnim.animatedSprites)

        elif (JuliusAnim.attackingGround(2) and not JuliusAnim.lockAttackAnim):
            JuliusAnim.attackAnim.playAnimation(Player.sprite, 20, JuliusAnim.animatedSprites)
            JuliusAnim.lockAttackAnim = True

        elif (JuliusAnim.attackingGround(1) and not JuliusAnim.lockAttackAnim):
            JuliusAnim.attackAnim.playAnimationFlipped(Player.sprite, 20, JuliusAnim.animatedSprites)
            JuliusAnim.lockAttackAnim = True

        elif (JuliusAnim.attackingAir(2)) and not JuliusAnim.lockAttackAnim:
            JuliusAnim.attackAirAnim.playAnimation(Player.sprite, 20, JuliusAnim.animatedSprites)
            JuliusAnim.lockAttackAnim = True

        elif (JuliusAnim.attackingAir(1) and not JuliusAnim.lockAttackAnim):
            JuliusAnim.attackAirAnim.playAnimationFlipped(Player.sprite, 20, JuliusAnim.animatedSprites)
            JuliusAnim.lockAttackAnim = True

        else:
            for animation in JuliusAnim.animatedSprites:
                if(animation.active):
                    animation.playAnimation(Player.sprite, 20, JuliusAnim.animatedSprites)
                elif(animation.activeFlipped):
                    animation.playAnimationFlipped(Player.sprite, 20, JuliusAnim.animatedSprites)
