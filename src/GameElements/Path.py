import random

import pygame

from src import Representations
from src.GameElements import Fork

displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

class Path:
    def __init__(self, levels):
        # Recieves the number of levels in the bifurcation network,
        # the number of exits in the network and the right exit
        self.numberOfLevels = levels
        self.numberOfExits = (2 ** levels)
        self.rightExit = random.randint(0, self.numberOfExits - 1)
        self.forkTree = []

        forkLength = (0.7 * displayWidth) / (self.numberOfLevels + 1)
        x_init = Representations.xInitialPos
        for i in range(levels + 1):
            randPosition = random.randint(0, 1)

            if randPosition == 1:
                randState = Representations.forkState["UP"]
            else:
                randState = Representations.forkState["DOWN"]

            if i == 0:
                forkHeight = 0 # The gate will be a straight horizontal line

                y_init = displayHeight / 2
                self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))

            else:
                forkHeight = (0.8 * displayHeight) / self.numberOfLevels
                x_init += forkLength
                j = 0
                while j < i:
                    if j == 0 or j == i-1:
                        y_init = (0.5 * displayHeight) + (((i - 1) / 2) * forkHeight) - (j * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        j += 1
                    else:
                        y_init = (0.5 * displayHeight) + (((i - 1) / 2) * forkHeight) - (j * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        y_init = (0.5 * displayHeight) + (((i - 1) / 2) * forkHeight) - ((j+1) * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        j += 2



    def plotPath(self):
        # Plots every fork of the path
        for fork in self.forkTree:
            fork.draw()