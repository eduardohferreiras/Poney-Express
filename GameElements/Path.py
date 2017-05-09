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
        self.forkTree = []

        for i in range((levels + 1):
            randPosition = random.randint(0, 1)
            randState = Representations.forkState["DOWN"]
            if randPosition == 1:
                randState = Representations.forkState["UP"]

            if i == 0:
                level_height = 0 # The gate will be a straight horizontal line
                x_init = Representations.x_init_player
                y_init = display_height / 2
                self.forkTree.append(Fork_Alternative.Fork_Alternative(gameDisplay, x_init, y_init, level_length, level_height, randState))

            else:
                level_height = (0.8 * display_height) / self.numberOfLevels
                x_init = Representations.x_init_player + level_length
                for j in range(i):
                    y_init = (0.5 * display_height) + (((i - 1) / 2) * level_height) - (j * level_height)
                    self.forkTree.append(Fork_Alternative.Fork_Alternative(gameDisplay, x_init, y_init, level_length, level_height, randState))



    def plotPath(self):
        # Plots every fork of the path
        for i in range(2 ** self.numberOfLevels):
            self.forkTree[i].draw()