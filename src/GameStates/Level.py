import pygame
from pygame.locals import *

from src import Representations
from src.GameElements import Path
from ..GameElements import Player

pygame.init()

#This class is responsible for activating the functionality related to the gameplay
class Level():
    def __init__(self):
        self.isPlaying = True
        self.difficulty = 1
        self.path = None
        self.player = None

    def set_background_image(self, file):
        self.backgroundImage = pygame.image.load(file)

    def text_objects(self, text, font, RGBcolor):
        textSurface = font.render(text, True, RGBcolor)
        return textSurface, textSurface.get_rect()

    def draw_level_dificulty(self):
        gameCanvas = pygame.display.get_surface()
        largeText = pygame.font.Font('src/Assets/Fonts/QuentinCaps.ttf', 85)
        levelTitleSurf, levelTitleRect = self.text_objects("Level " + str(self.difficulty), largeText, (0, 0, 0))
        levelTitleRect.center = ((gameCanvas.get_width() / 2 ), (gameCanvas.get_height() / 2 - 450))
        gameCanvas.blit(levelTitleSurf, levelTitleRect)

    def play_music(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1, 0)

    #This is the main function of the class, and is responsible for controlling the flow that the gameplay will show
    def execute_level(self):

        self.set_background_image('src/Assets/Images/Phase_1.jpg')
        path = Path.Path(self.difficulty)
        gameCanvas = pygame.display.get_surface()
        pygame.display.update()
        player = Player.Player(path)

        clock = pygame.time.Clock()
        counter = 0
        while self.isPlaying:

            if player.pathConcluded():
                if player.didWin(): #The player will move on to the next level
                    self.difficulty = self.difficulty + 1
                    return Representations.gameStates["GOING_TO_NEXT_LEVEL"]
                elif not player.didWin(): #The player will be moved to the game over menu
                    return Representations.gameStates["GAME_OVER"]
            elif not player.pathConcluded():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.isPlaying = False
                        return Representations.gameStates["SHUTTING DOWN"]
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            quit()
                            return Representations.gameStates["SHUTTING DOWN"]
                        elif event.key == K_SPACE: #Checks if user has clicked then toggles
                            player.toggle()
                player.step()
                gameCanvas.blit(self.backgroundImage, (0, 0))
                path.plotItems()
                self.draw_level_dificulty()
                player.draw(counter) #Counter is sent to draw() in order to aid in the selection of the player Sprite image
                path.plotPath()
                pygame.display.update()
                clock.tick(30)

                counter +=1