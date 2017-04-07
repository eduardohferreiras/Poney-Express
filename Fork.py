import pygame

class Fork():
    switch = True
    canToggle = True
    def __init__(self, x, y):
        self.image = pygame.Surface((50,10))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


    def toggle(self):
        if self.canToggle == True:
            if self.switch == True:
                self.rect.y -= 250;
                self.switch = False
            else:
                self.rect.y += 250;
                self.switch = True
