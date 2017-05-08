import pygame
from pygame.locals import *

from Engine import Player_Engine, Fork_Engine, Score_Engine
from UIElements import Start_Menu

pygame.init()


# Canvas
displayHeight = 1080
displayWidth = 1920
gameDisplay= pygame.display.set_mode((displayWidth,displayHeight),pygame.FULLSCREEN)
pygame.display.set_caption('Pony Express')


# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


fork = Fork_Engine.Fork(600, 700)
score = Score_Engine.Score()
player = Player_Engine.Player()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


#BackGround = Background('Nevada_Desert3.jpg', [0,0])

# Game starts


Start_Menu.StartMenu()



gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONUP:
            fork.toggle()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameExit = True


    # Updates
    score.update(gameDisplay)
    pygame.display.update()
    gameDisplay.fill([255, 255, 255])
    player.movePlayer(fork)
    #gameDisplay.blit(BackGround.image, BackGround.rect)
    gameDisplay.blit(fork.image, fork.rect)
    gameDisplay.blit(player.image, player.rect)


pygame.quit()
quit()