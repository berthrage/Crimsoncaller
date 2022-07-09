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
        JuliusAnim.setAnims2()

        if (Player.groundLevelX >= 6):
            Player.sprite.x -= 2000 * GameWindow.window.delta_time()
        if (Player.groundLevelX <= - 6):
            Player.sprite.x += 2000 * GameWindow.window.delta_time()
        if(Player.groundLevelX >= 5):
            Player.collidedWall = True
        else:
            Player.collidedWall = False

        ## WALKING
        if(not Player.still and Player.direction == 2 and Player.standing and not Player.collidedWall):
            if(Player.sprite.x < Level.scrollingLimit + 1 or Level.reachedLimitRight):
                Player.sprite.x += Player.walkSpeed * GameWindow.window.delta_time()



                if (Player.sprite.collided_perfect(Level1area1.tiles)):
                    Player.groundLevelX += Player.walkSpeed * GameWindow.window.delta_time()


        elif(not Player.still and Player.direction == 1 and Player.standing and not Player.collidedWall):
            if(Player.sprite.x > Level.scrollingLimit - 1 or Level.reachedLimitLeft):
                Player.sprite.x -= Player.walkSpeed * GameWindow.window.delta_time()

                if (Player.sprite.collided_perfect(Level1area1.tiles)):
                    Player.groundLevelX -= Player.walkSpeed * GameWindow.window.delta_time()

        if(not Player.sprite.collided_perfect(Level1area1.tiles)):
            Player.groundLevelX = 0

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

        Player.setGravity()

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

        if(not Player.still and Player.grounded and Player.sprite.collided_perfect(Level1area1.tiles) and Player.groundLevelY < 5 and not Player.collidedWall):
            Player.sprite.y -= 1000 * GameWindow.window.delta_time()
            Player.groundLevelY += 300 * GameWindow.window.delta_time()

        else:
            Player.groundLevelY = 0


        """if(not Player.still and Player.grounded and Player.sprite.collided_perfect(Level1area1.tiles)):
            Player.groundLevelX += Player.walkSpeed * GameWindow.window.delta_time()
        else:
            Player.groundLevelX = 0"""

        if(Player.sprite.rect.bottom >= Level1area1.tiles.rect.top):
            Player.collidedGround = True
        else:
            Player.collidedGround = False


        if((not Level1area1.tiles.collided_perfect(Player.sprite) and not Player.jumping) or Player.groundLevelY > 5):
            Player.sprite.y += Player.fallSpeed * GameWindow.window.delta_time()
            Player.fallSpeed += 200 * GameWindow.window.delta_time()

            Player.falling = True
        else:
            Player.fallSpeed = Player.tempFallSpeed
            Player.falling = False


        if((Player.falling and Player.freeFalling) or Player.jumping):
            Player.grounded = False
        else:
            Player.grounded = True


class JuliusAnim():
    animPaths = {
        "idle1_right": "sprites/player/right/julius-idle1-right.png",
        "idle1_left": Misc.strDirectionRtoL("sprites/player/right/julius-idle1-right.png"),

        "walk_right": "sprites/player/right/julius-walk-right.png",
        "walk_left": Misc.strDirectionRtoL("sprites/player/right/julius-walk-right.png"),

        "duck_right": "sprites/player/right/julius-duckstart-right2.png",
        "duck_left": Misc.strDirectionRtoL("sprites/player/right/julius-duckstart-right2.png"),

        "duckslide_right": "sprites/player/right/julius-duckslide-right2.png",
        "duckslide_left": Misc.strDirectionRtoL("sprites/player/right/julius-duckslide-right2.png"),

        "jumpmid_right": "sprites/player/right/julius-jumpmid-right.png",
        "jumpmid_left": Misc.strDirectionRtoL("sprites/player/right/julius-jumpmid-right.png"),

        "jumpmidstill_right": "sprites/player/right/julius-jumpmid-still-right.png",
        "jumpmidstill_left": Misc.strDirectionRtoL("sprites/player/right/julius-jumpmid-still-right.png"),

        "fall_right": "sprites/player/right/julius-fallstart-right.png",
        "fall_left": Misc.strDirectionRtoL("sprites/player/right/julius-fallstart-right.png"),

        "attack_right": "sprites/player/right/julius-attack-right.png",
        "attack_left": Misc.strDirectionRtoL("sprites/player/right/julius-attack-right.png"),

        "attackair_right": "sprites/player/right/julius-attackair-right.png",
        "attackair_left": Misc.strDirectionRtoL("sprites/player/right/julius-attackair-right.png"),
    }

    anims = {
        "idle1_right": False,
        "idle1_right_animChanged": False,
        "idle1_left": False,
        "idle1_left_animChanged": False,

        "walkstart_right": False,
        "walkstart_right_animChanged": False,
        "walkstart_left": False,
        "walkstart_left_animChanged": False,

        "walk_right": False,
        "walk_right_animChanged": False,
        "walk_left": False,
        "walk_left_animChanged": False,

        "duck_right": False,
        "duck_right_animChanged": False,
        "duck_left": False,
        "duck_left_animChanged": False,

        "duckslide_right": False,
        "duckslide_right_animChanged": False,
        "duckslide_left": False,
        "duckslide_left_animChanged": False,

        "jumpmid_right": False,
        "jumpmid_right_animChanged": False,
        "jumpmid_left": False,
        "jumpmid_left_animChanged": False,

        "jumpmidstill_right": False,
        "jumpmidstill_right_animChanged": False,
        "jumpmidstill_left": False,
        "jumpmidstill_left_animChanged": False,

        "fall_right": False,
        "fall_right_animChanged": False,
        "fall_left": False,
        "fall_left_animChanged": False,

        "attack_right": False,
        "attack_right_animChanged": False,
        "attack_left": False,
        "attack_left_animChanged": False,

        "attackair_right": False,
        "attackair_right_animChanged": False,
        "attackair_left": False,
        "attackair_left_animChanged": False,
    }


    animLists = {
        "idle1_right": [],
        "idle1_right_animChanged": False,
        "idle1_left": [],
        "idle1_left_animChanged": False,
    }

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

    timeElapsed = 0

    currentX = 0
    currentY = 0

    @staticmethod
    def changeAnim():
        pass

    @staticmethod
    def setAnims2():

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



    @staticmethod
    def setAnims():

        if (JuliusAnim.idling(2)):
            JuliusAnim.changeAnimation("idle1_right", 15, 80)
            # JuliusAnim.idle1_right = False
        elif (JuliusAnim.idling(1)):
            JuliusAnim.changeAnimation("idle1_left", 15, 80)
            # JuliusAnim.idle1_left = False
        elif (JuliusAnim.walking(2)):
            JuliusAnim.walkAnim("right")

        elif (JuliusAnim.walking(1)):
            JuliusAnim.walkAnim("left")
            JuliusAnim.timeElapsed += GameWindow.window.delta_time()

        elif (JuliusAnim.ducking(2)):
            JuliusAnim.changeAnimation("duck_right", 8, 70, False)

        elif (JuliusAnim.ducking(1)):
            JuliusAnim.changeAnimation("duck_left", 8, 70, False)

        elif (JuliusAnim.sliding(2)):
            JuliusAnim.changeAnimation("duckslide_right", 11, 30, False)

        elif (JuliusAnim.sliding(1)):
            JuliusAnim.changeAnimation("duckslide_left", 11, 30, False)

        elif (JuliusAnim.jumpingStill(2)):
            JuliusAnim.changeAnimation("jumpmidstill_right", 2, 70)

        elif (JuliusAnim.jumpingStill(1)):
            JuliusAnim.changeAnimation("jumpmidstill_left", 2, 70)

        elif (JuliusAnim.jumpingMoving(2)):
            JuliusAnim.changeAnimation("jumpmid_right", 2, 70)

        elif (JuliusAnim.jumpingMoving(1)):
            JuliusAnim.changeAnimation("jumpmid_left", 2, 70)

        elif (JuliusAnim.falling(2)):
            JuliusAnim.changeAnimation("fall_right", 10, 30, False)

        elif (JuliusAnim.falling(1)):
            JuliusAnim.changeAnimation("fall_left", 10, 30, False)

        elif (JuliusAnim.attackingGround(2)):
            if (not JuliusAnim.lockAttackAnim):
                JuliusAnim.changeAnimation("attack_right", 7, 50, False)
                JuliusAnim.lockAttackAnim = True

        elif (JuliusAnim.attackingGround(1)):
            if (not JuliusAnim.lockAttackAnim):
                JuliusAnim.changeAnimation("attack_left", 7, 50, False)
                JuliusAnim.lockAttackAnim = True

        elif (JuliusAnim.attackingAir(2)):
            if (not JuliusAnim.lockAttackAnim):
                JuliusAnim.changeAnimation("attackair_right", 7, 50, False)
                JuliusAnim.lockAttackAnim = True

        elif (JuliusAnim.attackingAir(1)):
            if (not JuliusAnim.lockAttackAnim):
                JuliusAnim.changeAnimation("attackair_left", 7, 50, False)
                JuliusAnim.lockAttackAnim = True



    @staticmethod
    def changeAnimation(animation, maxFrames, animTime=10, loop=True):
        JuliusAnim.anims[animation] = True

        if (JuliusAnim.anims[animation] and not JuliusAnim.anims[animation + "_animChanged"]):
            currentX = Player.sprite.x
            currentY = Player.sprite.y


            if(maxFrames > 1):
                Player.sprite = Sprite(JuliusAnim.animPaths[animation], maxFrames)
                Player.sprite.set_sequence_time(0, maxFrames, animTime, loop)
            else:
                Player.sprite = Sprite(JuliusAnim.animPaths[animation])

            Player.sprite.set_position(currentX, currentY)

            JuliusAnim.anims[animation + "_animChanged"] = True
            JuliusAnim.anims[animation] = False

            for anim in JuliusAnim.anims:
                if(anim != animation + "_animChanged"):
                   JuliusAnim.anims[anim] = False

    @staticmethod
    def walkAnim(directionStr):
        timeElapsed = 0
        JuliusAnim.changeAnimation("walk_" + directionStr, 16, 40)
        JuliusAnim.changeAnimation("walk_" + directionStr, 16, 40)


