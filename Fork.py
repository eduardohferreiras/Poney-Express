import pygame

class Fork():
    switch = True
    def __init__(self):
        self.image = pygame.Surface((100,10))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100

    def toggle(self):
        if self.switch == True:
            self.rect.y += 10;
            self.switch = False
        else:
            self.rect.y -= 10;
            self.switch = True
