import pygame
from pygame.locals import *

from src import Representations
from src.GameStates import Menu

pygame.init()

class Start_Menu(Menu.Menu):

    def execute_menu(self):
        #First, we set the background image and the song.
        pygame.init()
        self.set_background_image('src/Assets/Images/Start_Menu_Background.jpg')
        self.play_music("src/Assets/Sounds/themeSong.mp3")
        gameCanvas = pygame.display.get_surface()

        clock = pygame.time.Clock()

        while self.isInMenu:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:# if the current event is to quit the game, then we quit the loop and return the correct gameState
                    self.isInMenu = False
                    return Representations.gameStates["SHUTTING DOWN"]
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:# if the user press ESC, the game closes
                        pygame.quit()
                        quit()
                        return Representations.gameStates["SHUTTING DOWN"]
                    elif event.key == K_SPACE:# if the user press Space, the intruction screen starts.
                        self.isInMenu = False
                        return Representations.gameStates["ON_INSTRUCTIONS"]
                    else: #If not of this happens, we set the texts and images of the start menu screen.
                        gameCanvas.fill((0, 0, 0))
                        gameCanvas.blit(self.backgroundImage, (0, 0))

                        largeText = pygame.font.Font('src/Assets/Fonts/QuentinCaps.ttf', 150)
                        notSoLargeText = pygame.font.Font('src/Assets/Fonts/BillyTheKid.ttf', 70)

                        titleSurf, titleRect = self.text_objects("Poney Express", largeText, (0, 0, 0))
                        titleRect.center = ((gameCanvas.get_width() / 2 + 330), (gameCanvas.get_height() / 2 - 300))

                        subTitleSurf, subTitleRect = self.text_objects("Press Space if you dare", notSoLargeText,
                                                                       (216, 212, 212))
                        subTitleRect.center = (gameCanvas.get_width() / 2, (gameCanvas.get_height() / 2 + 200))

                        gameCanvas.blit(subTitleSurf, subTitleRect)
                        gameCanvas.blit(titleSurf, titleRect)

                        pygame.display.update()
                        clock.tick(30)

                elif event.type != KEYDOWN: # For a bug free gaming experience, it was necessary to repeat the upper code block.
                    gameCanvas.fill((0, 0, 0))
                    gameCanvas.blit(self.backgroundImage, (0, 0))

                    largeText = pygame.font.Font('src/Assets/Fonts/QuentinCaps.ttf', 150)
                    notSoLargeText = pygame.font.Font('src/Assets/Fonts/BillyTheKid.ttf', 70)

                    titleSurf, titleRect = self.text_objects("Poney Express", largeText, (0, 0, 0))
                    titleRect.center = ((gameCanvas.get_width() / 2 + 330), (gameCanvas.get_height() / 2 - 300))

                    subTitleSurf, subTitleRect = self.text_objects("Press Space if you dare", notSoLargeText,
                                                                   (216, 212, 212))
                    subTitleRect.center = (gameCanvas.get_width() / 2, (gameCanvas.get_height() / 2 + 200))

                    gameCanvas.blit(subTitleSurf, subTitleRect)
                    gameCanvas.blit(titleSurf, titleRect)

                    pygame.display.update()
                    clock.tick(60)