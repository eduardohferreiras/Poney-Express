import pygame
from pygame.locals import *

from src import Representations
from src.GameElements import Path
from ..GameElements import Player

pygame.init()

class Level():
    def __init__(self):
        self.isPlaying = True
        self.difficulty = 2
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

    def execute_level(self):

        self.set_background_image('src/Assets/Images/Phase_1.jpg')
        path = Path.Path(self.difficulty)
        player = Player.Player(path)
        gameCanvas = pygame.display.get_surface()

        clock = pygame.time.Clock()
        counter = 0
        while self.isPlaying:

            if player.pathConcluded():
                if player.didWin():
                    self.difficulty = self.difficulty + 1
                    return Representations.gameStates["GOING_TO_NEXT_LEVEL"]
                elif not player.didWin():
                    return Representations.gameStates["GAME_OVER"]
            elif not player.pathConcluded():
                #Ver se clicou, dar step, atualizar tudo, dar display.update(), blit?.
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.isPlaying = False
                        return Representations.gameStates["SHUTTING DOWN"]
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            quit()
                            return Representations.gameStates["SHUTTING DOWN"]
                        elif event.key == K_SPACE:
                            player.toggle()
                player.step()
                gameCanvas.blit(self.backgroundImage, (0,0))
                self.draw_level_dificulty()
                player.draw(counter)
                path.plotPath()
                pygame.display.update()
                clock.tick(30)

                counter +=1