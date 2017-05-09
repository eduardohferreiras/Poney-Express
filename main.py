import pygame
from pygame.locals import *

import Representations
from GameElements import Player, Fork_Engine, Score
from GameStates import Start_Menu
from UIElements import Canvas


#Se livrar dessa porra
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#BackGround = Background('Nevada_Desert3.jpg', [0,0])


pygame.init()

#Inicialização das classes
canvas = Canvas.Canvas(1080, 1920)
fork = Fork_Engine.Fork(600, 700)
score = Score.Score()
player = Player.Player()
startMenu = Start_Menu.Start_Menu()

# Setando o display do jogo.
canvas.set_canvas()

#Setando o primeiro Game_State
currentGameState = Representations.gameStates['ON_START_MENU']

startMenu.execute_menu()

#globalGameExit = False
#while not globalGameExit:
#    if currentGameState == Representations.gameStates["ON_START_MENU"]:
#        currentGameState = startMenu.execute_menu()
#    elif currentGameState == Representations.gameStates["ON_GAMEPLAY"]:
#        currentGameState = startMenu.execute_menu()





#Esse gameExit deveria ser "gameplayExit" e o código abaixo deverá estar na classe gameplayDisplay(?)
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONUP:
            fork.toggle()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gameExit = True

pygame.quit()
quit()
