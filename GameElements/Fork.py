import pygame
import random

Fork_Color = (132, 60, 12)

class Fork_Alternative:

    def __init__(self, x_init, y_init, level_length, level_height):
        self.x_init = x_init
        self.y_init = y_init
        self.level_length = level_length
        self.level_height = level_height

        # Starts with a random initial configuration for the gate
        up_down = round(random.randint(0,1))
        self.up_down = up_down
        if self.up_down == 0:
            self.x_end = self.x_init + self.level_length
            self.y_end = self.y_init +(self.level_height / 2)
        else:
            self.x_end = self.x_init + self.level_length
            self.y_end = self.y_init - (self.level_height / 2)


    def draw(self):
        # Plots the lines of the gates
        pygame.draw.line(pygame.display.get_surface(), Fork_Color, (self.x_init, self.y_init), (self.x_end, self.y_end), 5)

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

