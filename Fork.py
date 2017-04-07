import pygame

class Fork():
    def __init__(self):
        self.image = pygame.Surface((100,10))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100