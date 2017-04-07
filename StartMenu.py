import pygame
from pygame.locals import *

pygame.init()

def StartMenu():
    isInStartMenu = True

    #displayWidth e displayHeight seram atributos da classe render.

    displayHeight = 1080
    displayWidth = 1920
    gameDisplay= pygame.display.set_mode((displayWidth,displayHeight),pygame.FULLSCREEN)
    pygame.display.toggle_fullscreen()
    startMenuImg = pygame.image.load('Assets/Images/Start_Menu_Background.jpg')

    clock = pygame.time.Clock()

    while isInStartMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isInStartMenu = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_RETURN:
                    isInStartMenu = False;

        gameDisplay.fill((0,0,0))
        gameDisplay.blit(startMenuImg ,(0,0))
        pygame.display.update()
        clock.tick(60)


