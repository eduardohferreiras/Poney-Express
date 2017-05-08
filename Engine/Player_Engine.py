import pygame

class Player():
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 550

    def movePlayer(self, fork):
        if self.rect.x < 1700:
            self.rect.x += 1
        if fork.rect.x >= (self.rect.x - 5) and fork.rect.x <= (self.rect.x):
            fork.canToggle = False
            if fork.switch == True:
                self.rect.y += 135
            else:
                self.rect.y -= 120