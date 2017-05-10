import pygame

class Canvas():
    def __init__(self, canvasHeight, canvasWidth):
        self.canvasHeight = canvasHeight
        self.canvasWidth = canvasWidth

    def set_canvas(self):
        self.gameCanvas = pygame.display.set_mode((self.canvasWidth, self.canvasHeight), pygame.FULLSCREEN)
        pygame.display.set_caption('Pony Express')