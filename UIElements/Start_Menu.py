import pygame
from pygame.locals import *

pygame.init()


def text_objects(text, font, RGBcolor):
    textSurface = font.render(text, True, RGBcolor)
    return textSurface, textSurface.get_rect()

def StartMenu():
    isInStartMenu = True

    #displayWidth e displayHeight seram atributos da classe render.

    displayHeight = 1080
    displayWidth = 1920
    gameDisplay= pygame.display.set_mode((displayWidth,displayHeight),pygame.FULLSCREEN)
    pygame.display.toggle_fullscreen()
    startMenuImg = pygame.image.load('Assets/Images/Start_Menu_Background.jpg')

    pygame.mixer.music.load("Assets/Sounds/themeSong.mp3")
    pygame.mixer.music.play(10, 0)

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

        largeText = pygame.font.Font('Assets/Fonts/QuentinCaps.ttf',150)
        notSoLargeText = pygame.font.Font('Assets/Fonts/BillyTheKid.ttf',70)

        titleSurf, titleRect = text_objects("Poney Express", largeText, (0,0,0))
        titleRect.center = ((displayWidth/2+330),(displayHeight/2-300))

        subTitleSurf, subTitleRect = text_objects("Press Enter if you dare", notSoLargeText, (216,212,212))
        subTitleRect.center = (displayWidth/2,(displayHeight/2+200))

        gameDisplay.blit(subTitleSurf,subTitleRect)
        gameDisplay.blit(titleSurf,titleRect)

        pygame.display.update()
        clock.tick(60)


