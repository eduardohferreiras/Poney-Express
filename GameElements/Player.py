from GameElements import Path
import pygame
import Representations
import math

playerColor = (132, 3, 20)
display_width = 800
display_height = 600

playerRadius = 10
stepSize = 1.0

class Player:
    # This class is resposible for the main character, the player of the game
    def __init__(self, path):
        self.gameSurface = pygame.display.get_surface()
        self.path = path
        self.xPos = Representations.x_init_player
        self.yPos = display_height / 2

    def draw(self):
    # plots the player in the display
    pygame.draw.circle(self.gameSurface, playerColor, (self.xPos, self.yPos), playerRadius)

    def step(self):
    # player is one step closer to the end of the game
    self.xPos += stepSize
    levelLenght = 0.7 * display_width / (self.path.numberOfLevels + 1)
    if self.xPos > (levelLenght + Representations.x_init_player): # In this case yPos changes
        levelHeight = 0.8 * display_height / self.path.numberOfLevels
        tangent = levelHeight / (2 * levelLenght)

        xFork = math.floor((self.xPos - Representations.x_init_player)/ (levelLenght))
        yFork = (xFork - 1) - math.floor((self.yPos - (display_height/2)) / (levelHeight / 2))

        if (self.xPos - Representations.x_init_player) / (levelLenght) - math.floor((self.xPos - Representations.x_init_player) / (levelLenght)) == 0:
            xFork = math.floor((self.xPos - stepSize - Representations.x_init_player)/ (levelLenght))
            yFork = (xFork - 1) - math.floor((self.yPos - (display_height/2)) / (levelHeight / 2))

        if self.path.matrix[xFork][yFork] == 1: # Fork is up
            self.yPos += tangent * stepSize
        else: # Fork is down
            self.yPos -= tangent * stepSize


    def toggle(self):
    # toggles the next forks of the path