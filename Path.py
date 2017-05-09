import pygame
from Engine import Fork_Alternative
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
background_Image = pygame.image.load('Assets/Images/Phase_1.jpg')



Fork_Color = (132, 60, 12)
x_init_player = 30


class Path:
    def __init__(self, levels):
        self.numberOfLevels = levels
        self.numberOfExits = (2 ** levels)
        self.rightExit = random.randint(0, self.numberOfExits - 1)

    def plotPath(self):
        level_length = (0.7 * display_width) / (self.numberOfLevels + 1)
        for i in range(self.numberOfLevels + 1):
            if i == 0:
                level_height = 0
                x_init = x_init_player
                y_init = display_height / 2
                fork = Fork_Alternative.Fork_Alternative(gameDisplay, x_init, y_init, level_length, level_height)
                fork.draw()
            else:
                level_height = (0.8 * display_height) / level_length
                x_init = x_init + level_length
                for j in range(i):
                    y_init = (0.5 * display_height) + (((i - 1) / 2) * level_height) - (j * level_height)
                    fork = Fork_Alternative(gameDisplay, x_init, y_init, level_length, level_height)
                    fork.draw()


p = Path(1)
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            gameExit = True
    gameDisplay.blit(background_Image, (0,0))
    p.plotPath()
    pygame.display.update()