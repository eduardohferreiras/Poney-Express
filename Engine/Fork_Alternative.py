import pygame
import random

Fork_Color = (132, 60, 12)

# TESTES
# pygame.init()
#
# display_width = 800
# display_height = 600
# gameDisplay = pygame.display.set_mode((display_width, display_height))
# background_Image = pygame.image.load('../Assets/Images/Phase_1.jpg')


class Fork_Alternative:

    def __init__(self, game_surface, x_init, y_init, level_length, level_height):
        # Recieves "gameDisplay" and the rest of parametes of Path
        self.image = game_surface
        self.x_init = x_init
        self.y_init = y_init
        self.level_length = level_length
        self.level_height = level_height
        # Starts with a random initial configuration for the gates
        up_down = round(random.randint(0,1))
        self.up_down = up_down
        if self.up_down == 0:
            self.x_end = self.x_init + self.level_length
            self.y_end = self.y_init - (self.level_height / 2)
        else:
            self.x_end = self.x_init + self.level_length
            self.y_end = self.y_init + (self.level_height / 2)

    def getArrayElement(self):
        return self.up_down

    def draw(self):
        # Plots the lines of the gates
        pygame.draw.line(self.image, Fork_Color, (self.x_init, self.y_init), (self.x_end, self.y_end), 5)

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


# TESTES
# p = Fork_Alternative(gameDisplay, 100, 300, 50, 50)
# gameExit = False
# while not gameExit:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             gameExit = True
#     gameDisplay.blit(background_Image, (0,0))
#     p.draw()
#     pygame.display.update()