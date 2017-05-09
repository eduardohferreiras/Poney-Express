import pygame, Representations
from Engine import Fork_Alternative
import random

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
        for i in range(levels + 1):
            randPosition = random.randint(0, 1)
            randState = Representations.forkState["DOWN"]
            if randPosition == 1:
                randState = Representations.forkState["UP"]

            if i == 0:
                forkHeight = 0 # The gate will be a straight horizontal line
                x_init = Representations.xInitialPos
                y_init = displayHeight / 2
                self.forkTree.append(Fork_Alternative.Fork_Alternative(gameDisplay, x_init, y_init, forkLength, forkHeight, randState))

            else:
                forkHeight = (0.8 * displayHeight) / self.numberOfLevels
                x_init = Representations.xInitialPos + forkLength
                for j in range(i):
                    y_init = (0.5 * displayHeight) + (((i - 1) / 2) * forkHeight) - (j * forkHeight)
                    self.forkTree.append(Fork_Alternative.Fork_Alternative(gameDisplay, x_init, y_init, forkLength, forkHeight, randState))



    def plotPath(self):
        # Plots every fork of the path
        for i in range(2 ** self.numberOfLevels):
            self.forkTree[i].draw()