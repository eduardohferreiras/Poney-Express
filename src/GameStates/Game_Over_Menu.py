import pygame
from src.GameStates import Menu
from src import Representations
from pygame.locals import *


class Game_Over_Menu(Menu.Menu):
    def execute_menu(self):
        #First, we update change the background image and the music.
        self.set_background_image("src/Assets/Images/Atomic Bomb.jpg")
        self.play_music("src/Assets/Sounds/Explosion.wav")
        gameCanvas = pygame.display.get_surface()

        clock = pygame.time.Clock()

        while self.isInMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:# if the current event is to quit the game, then we quit the loop and return the correct gameState
                    self.isInMenu = False
                    return Representations.gameStates["GAME_OVER"]
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:# if the user press Space, the game closes.
                        pygame.quit()
                        quit()
                        return Representations.gameStates["GAME_OVER"]
            # Here, we print the texts and update the screen.
            gameCanvas.fill((0, 0, 0))
            gameCanvas.blit(self.backgroundImage, (0, 0))

            largeText = pygame.font.Font('src/Assets/Fonts/QuentinCaps.ttf', 150)
            notSoLargeText = pygame.font.Font('src/Assets/Fonts/BillyTheKid.ttf', 70)

            titleSurf, titleRect = self.text_objects("YOU DIED", largeText, (0, 0, 0))
            titleRect.center = (gameCanvas.get_width() / 2, gameCanvas.get_height() / 2)

            subTitleSurf, subTitleRect = self.text_objects("Press ESC to to close", notSoLargeText,
                                                           (50, 50, 50))
            subTitleRect.center = (gameCanvas.get_width() / 2, (gameCanvas.get_height() / 2 + 200))

            gameCanvas.blit(subTitleSurf, subTitleRect)
            gameCanvas.blit(titleSurf, titleRect)

            pygame.display.update()
            clock.tick(30)