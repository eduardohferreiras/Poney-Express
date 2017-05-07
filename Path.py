import pygame
import Fork
import random

class Path():
    def __init__(self, levels):
        self.numberOfLevels = levels
        self.numberOfExits = (2 ** levels)
        self.rightExit = random.randint(0, self.numberOfExits - 1)

    def plotPath:
