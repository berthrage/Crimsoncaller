from PPlay.sprite import *

class AnimatedSprite():
    def __init__(self):
        self.sprites = []
        self.currentFrame = 0
        self.currentFrameFlipped = 0
        self.active = False
        self.activeFlipped = False

    def playAnimation(self, sprite, animationSpeed=1, animationlist=None, loop=True):
        positionX = sprite.x
        positionY = sprite.y



        from GameWindow import GameWindow
        self.currentFrame += animationSpeed * GameWindow.window.delta_time()

        if self.currentFrame >= len(self.sprites) and loop:
            self.currentFrame = 0
        elif self.currentFrame >= len(self.sprites) and not loop:
            self.currentFrame = len(self.sprites) - 1


        spriteImage = self.sprites[int(self.currentFrame)].image
        sprite.image = spriteImage
        sprite.mask = pygame.mask.from_surface(spriteImage)
        sprite.rect = spriteImage.get_rect()
        sprite.set_position(positionX, positionY)

        if(isinstance(animationlist, list)):
            self.resetAllAnimations(animationlist)

        sprite.draw()
        #sprite.update()

    def playAnimationFlipped(self, sprite, animationSpeed=1, animationlist=None, loop=True):
        positionX = sprite.x
        positionY = sprite.y
        from GameWindow import GameWindow
        self.currentFrameFlipped += animationSpeed * GameWindow.window.delta_time()

        if self.currentFrameFlipped >= len(self.sprites) and loop:
            self.currentFrameFlipped = 0
        elif self.currentFrameFlipped >= len(self.sprites) and not loop:
            self.currentFrameFlipped = len(self.sprites) - 1

        spriteImage = self.sprites[int(self.currentFrameFlipped)].image
        spriteFlipped = pygame.transform.flip(spriteImage, True, False)
        sprite.image = spriteFlipped
        sprite.mask = pygame.mask.from_surface(spriteFlipped)
        sprite.rect = spriteFlipped.get_rect()
        sprite.set_position(positionX, positionY)

        if (isinstance(animationlist, list)):
            self.resetAllAnimations(animationlist, True)

        sprite.draw()

    def addSprite(self, folderPath, numberofFrames):
        for i in range(numberofFrames):
            self.sprites.append(Sprite(f"{folderPath}/{i+1}.png"))


    def resetAllAnimations(self, animatedSprites, flipped=False):
        if(not flipped):
            self.active = True
            self.activeFlipped = False

            for animation in animatedSprites:
                if(animation != self):
                    animation.currentFrame = 0
                    animation.active = False
                    animation.activeFlipped = False
                animation.currentFrameFlipped = 0
        else:
            self.active = False
            self.activeFlipped = True

            for animation in animatedSprites:
                if(animation != self):
                    animation.currentFrameFlipped = 0
                    animation.active = False
                    animation.activeFlipped = False
                animation.currentFrame = 0