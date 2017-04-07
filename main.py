import pygame
import Fork

pygame.init()


# Canvas
gameDisplay = pygame.display.set_mode((1024,671))
pygame.display.set_caption('Pony Express')


# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)



fork = Fork.Fork()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


#BackGround = Background('Nevada_Desert3.jpg', [0,0])

# Game starts
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONUP:
            if fork.rect.y == 100:
                fork.rect.y += 10
            else:
                fork.rect.y -= 10;

    # Where we print stuff on screen
    pygame.display.update()
    gameDisplay.fill([255, 255, 255])
#    gameDisplay.blit(BackGround.image, BackGround.rect)
    gameDisplay.blit(fork.image, fork.rect)


pygame.quit()
quit()