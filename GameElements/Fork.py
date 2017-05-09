import pygame, Representations, random

class Fork_Alternative:

    def __init__(self, x_init, y_init, level_length, level_height, forkState):
        self.x_init = x_init
        self.y_init = y_init
        self.level_length = level_length
        self.level_height = level_height
        self.forkState = forkState

        if self.forkState == Representations.forkState["DOWN"]:
            self.x_end = self.x_init + self.level_length
            self.y_end = self.y_init +(self.level_height / 2)
        else:
            self.x_end = self.x_init + self.level_length
            self.y_end = self.y_init - (self.level_height / 2)


    def draw(self):
        # Plots the lines of the gates
        pygame.draw.line(pygame.display.get_surface(), Representations.Fork_Color, (self.x_init, self.y_init), (self.x_end, self.y_end), 5)

    def toggle(self):
        # Alternates gates
        if self.up_down == 0:
            self.up_down = 1
            self.x_end = self.x_init + self.level_length
            self.y_end = self.y_init + (self.level_height / 2)
        else:
            self.up_down = 0
            self.x_end = self.x_init + self.level_length
            self.y_end = self.y_init - (self.level_height / 2)

