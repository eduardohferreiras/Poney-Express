import pygame

#Colors
white = (255, 255, 255)
black = (0, 0, 0)

def getFont(name = "Courier New", size = 20, style = ''): # Returns the font we want
    return pygame.font.SysFont(name, size, style)

class Score():

    level = 1

    def __init__(self):
        self.image = pygame.Surface((150, 250))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = 850
        self.rect.y = 0


    def writeLevel(self):
        text = getFont(size = 40).render(("Level: " + str(Score.level)), True, black)
        self.image.blit(text, (5, 10))


    def update(self, gameDisplay):
        self.writeLevel()
        gameDisplay.blit(self.image, self.rect)


