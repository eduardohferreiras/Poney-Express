import pygame, Representations, random

class Fork_Alternative:

    def __init__(self, xStart, yStart, forkLength, forkHeight, forkState):
        self.xStart = xStart
        self.yStart = yStart
        self.forkLength = forkLength
        self.forkHeight = forkHeight
        self.forkState = forkState

        if self.forkState == Representations.forkState["DOWN"]:
            self.xEnd = self.xStart + self.forkLength
            self.yEnd = self.yStart + (self.forkHeight / 2)
        else:
            self.xEnd = self.xStart + self.forkLength
            self.yEnd = self.yStart - (self.forkHeight / 2)


    def draw(self):
        # Plots the lines of the gates
        pygame.draw.line(pygame.display.get_surface(), Representations.Fork_Color, (self.xStart, self.yStart), (self.xEnd, self.yEnd), 5)

    def toggle(self):
        # Alternates gates
        if self.forkState == 0:
            self.forkState = 1
            self.xEnd = self.xStart + self.forkLength
            self.yEnd = self.yStart + (self.forkHeight / 2)
        else:
            self.forkState = 0
            self.xEnd = self.xStart + self.forkLength
            self.yEnd = self.yStart - (self.forkHeight / 2)

