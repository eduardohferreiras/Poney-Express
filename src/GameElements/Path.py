import random
import math
import pygame

from src import Representations
from src.GameElements import Fork

class Path:
    def __init__(self, levels):
        # Recieves the number of levels in the bifurcation network,
        # the number of exits in the network and the right exit
        self.numberOfLevels = levels
        self.numberOfExits = levels + 1
        self.rightExit = random.randint(0, self.numberOfExits - 1)
        self.forkTree = []
        self.gameDisplay = pygame.display.get_surface()

        forkLength = (0.7 * self.gameDisplay.get_width()) / (self.numberOfLevels + 1)
        x_init = Representations.xInitialPos
        for i in range(levels + 1):
            randPosition = random.randint(0, 1)

            if randPosition == 1:
                randState = Representations.forkState["UP"]
            else:
                randState = Representations.forkState["DOWN"]

            if i == 0:
                forkHeight = 0 # The gate will be a straight horizontal line

                y_init = self.gameDisplay.get_height()/ 2
                self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))

            else:
                forkHeight = (0.8 * self.gameDisplay.get_height()) / self.numberOfLevels
                x_init += forkLength
                j = 0
                while j < i:
                    if j == 0 or j == i-1:
                        y_init = (0.5 * self.gameDisplay.get_height()) + (((i - 1) / 2) * forkHeight) - (j * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        j += 1
                    else:
                        y_init = (0.5 * self.gameDisplay.get_height()) + (((i - 1) / 2) * forkHeight) - (j * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        y_init = (0.5 * self.gameDisplay.get_height()) + (((i - 1) / 2) * forkHeight) - ((j+1) * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        j += 2


    def plotPath(self):
        # Plots every fork of the path
        for fork in self.forkTree:
            fork.draw()

    def plotItems(self):
        forkHeight = (0.7* self.gameDisplay.get_height()) / self.numberOfLevels
        gold = pygame.image.load("src/Assets/Images/Gold_Final.png")
        bomb = pygame.image.load("src/Assets/Images/Bombs_Final.png")
        index = 2 ** (self.numberOfLevels - 1)
        firstX = self.forkTree[index].xEnd
        firstY = self.gameDisplay.get_height()*0.1
        # print("xPos = {0}; yPos = {1}".format(firstX, firstY))
        # print("height = {0}".format(forkHeight))
        for i in range(self.numberOfExits):
            if i == self.rightExit:
                self.gameDisplay.blit(gold, (firstX, firstY + i*forkHeight))
            else:
                self.gameDisplay.blit(bomb, (firstX, firstY + i*forkHeight))