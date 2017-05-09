import pygame
from pygame.locals import *

import Representations
from GameElements import Player, Fork_Engine, Score
from GameStates import Start_Menu, Level, Game_Over_Menu
from UIElements import Canvas

pygame.init()

#Inicialização das classes
canvas = Canvas.Canvas(1080, 1920)
fork = Fork_Engine.Fork(600, 700)
score = Score.Score()
player = Player.Player()
currentLevel = Level.Level()
startMenu = Start_Menu.Start_Menu()
gameOverMenu = Game_Over_Menu().Game_Over_Menu()

# Setando o display do jogo.
canvas.set_canvas()

#Setando o primeiro Game_State
currentGameState = Representations.gameStates['ON_START_MENU']

startMenu.execute_menu()

globalGameExit = False
while not globalGameExit:
   if currentGameState == Representations.gameStates["ON_START_MENU"]:
       currentGameState = startMenu.execute_menu()
   elif currentGameState == Representations.gameStates["ON_GAMEPLAY"]:
       currentGameState = currentLevel.execute_level()
   elif currentGameState == Representations.gameStates["GOING_TO_NEXT_LEVEL"]:
       currentGameState = currentLevel.execute_level()
   elif currentGameState == Representations.gameStates["GAME_OVER"]:
       currentGameState = gameOverMenu.execute_menu()



# #Esse gameExit deveria ser "gameplayExit" e o código abaixo deverá estar na classe gameplayDisplay(?)
# gameExit = False
# while not gameExit:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             gameExit = True
#         if event.type == pygame.MOUSEBUTTONUP:
#             fork.toggle()
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 gameExit = True

pygame.quit()
quit()
