import pygame
from pygame.locals import *

import Representations
from GameElements import Player, Path, Score
from GameStates import Start_Menu, Level, Game_Over_Menu
from UIElements import Canvas

pygame.init()

#Inicialização das classes
canvas = Canvas.Canvas(1080, 1920)
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

pygame.quit()
quit()
