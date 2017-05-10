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

        # Length of each Fork
        forkLength = (0.8 * self.gameDisplay.get_width()) / (self.numberOfLevels + 1)
        x_init = Representations.xInitialPos # Initial position in x axis

        # We need to create every Fork object and then append them
        # to the forkTree array.
        # In the end we need to add 2**levels Forks to the array, due to the
        # structure data used in this implementation
        for i in range(levels + 1):

            # Initialize a random position (up or down) to the Fork
            randPosition = random.randint(0, 1)
            if randPosition == 1:
                randState = Representations.forkState["UP"]
            else:
                randState = Representations.forkState["DOWN"]

            if i == 0: # First fork is alway a horizontal line with the two states (up and down) being the same
                forkHeight = 0 # The gate will be a straight horizontal line

                y_init = self.gameDisplay.get_height()/ 2
                self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))

            else: # All the other Forks
                forkHeight = (0.8 * self.gameDisplay.get_height()) / self.numberOfLevels
                x_init += forkLength

                counter = 0
                j = 0
                while j < i:
                    if j == 0 or j == i - 1:
                        y_init = (0.5 * self.gameDisplay.get_height()) + (((i - 1) / 2) * forkHeight) - (j * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        j += 1
                    else:
                        y_init = (0.5 * self.gameDisplay.get_height()) + (((i - 1) / 2) * forkHeight) - (j * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        y_init = (0.5 * self.gameDisplay.get_height()) + (((i - 1) / 2) * forkHeight) - (
                        (j + 1) * forkHeight)
                        self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                        j += 2
                    counter = j

                # Due to the data structure, we need to repeat some
                # Forks so the game can ran smoother
                while counter < 2 ** (i - 1):
                    y_init = (0.5 * self.gameDisplay.get_height()) + (((i - 1) / 2) * forkHeight) - (0 * forkHeight)
                    self.forkTree.append(Fork.Fork(x_init, y_init, forkLength, forkHeight, randState))
                    counter += 1



    def plotPath(self):
        # Plots every fork of the path
        for fork in self.forkTree:
            fork.draw()

    def plotItems(self):
        # Plots the items in the end of each possible way: gold or bombs
        forkHeight = (0.8* self.gameDisplay.get_height()) / self.numberOfLevels
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