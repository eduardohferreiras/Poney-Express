import pygame

pygame.init()


# Canvas
gameDisplay = pygame.display.set_mode((1024,671))
pygame.display.set_caption('Pony Express')


# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('Nevada_Desert3.jpg', [0,0])


gameExit = False

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    pygame.display.update()
    gameDisplay.fill([255, 255, 255])
    gameDisplay.blit(BackGround.image, BackGround.rect)

    clock.tick(15)
