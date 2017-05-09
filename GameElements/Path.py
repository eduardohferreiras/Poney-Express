import pygame, Representations
from Engine import Fork_Alternative
import random

pygame.init()

class Path:
    def __init__(self, levels):
        # Recieves the number of levels in the bifurcation network,
        # the number of exits in the network and the right exit
        self.numberOfLevels = levels
        self.numberOfExits = (2 ** levels)
        self.rightExit = random.randint(0, self.numberOfExits - 1)

    def plotPath(self):
        # Calls the Fork class every time it needs to draw an alternating gate,
        # (up and down). It needs to define "x_init" and "y_init" (gate's initial
        # coordinates, "x_end" and "y_end" (gate's final coordinates) and level_length
        # and level_height (the length and height of each gate)

        self.matrix = [[0 for x in range(self.numberOfLevels)] for y in range(self.numberOfLevels)]

        level_length = (0.7 * display_width) / (self.numberOfLevels + 1)

        for i in range(self.numberOfLevels + 1):
            if i == 0:
                level_height = 0 # The gate will be a straight horizontal line
                x_init = Representations.x_init_player
                y_init = display_height / 2
                fork = Fork_Alternative.Fork_Alternative(gameDisplay, x_init, y_init, level_length, level_height)
                self.matrix[i][0] = fork.getArrayElement()
                fork.draw()
            else:
                level_height = (0.8 * display_height) / self.numberOfLevels
                x_init = x_init + level_length
                for j in range(i):
                    y_init = (0.5 * display_height) + (((i - 1) / 2) * level_height) - (j * level_height)
                level_height = (0.8 * display_height) /(self.numberOfLevels)
                x_init = x_init + level_length
                for j in range(i):
                    y_init = (0.5 * display_height) + (((i - 1) / 2) * level_height) - (j * level_height)
                    fork = Fork_Alternative.Fork_Alternative(gameDisplay, x_init, y_init, level_length, level_height)
                    self.matrix[i][j] = fork.getArrayElement()
                    fork.draw()

