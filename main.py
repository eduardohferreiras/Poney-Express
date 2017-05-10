import pygame

from src import Representations
from src.GameElements import Canvas
from src.GameStates import Level, Start_Menu, Game_Over_Menu, Opening_Instructions

pygame.init()

#Inicialização das classes
canvas = Canvas.Canvas(1080, 1920)
currentLevel = Level.Level()
openingInstructions = Opening_Instructions.Opening_Instructions()
startMenu = Start_Menu.Start_Menu()
gameOverMenu = Game_Over_Menu.Game_Over_Menu()

# Setando o display do jogo.
canvas.set_canvas()

#Setando o primeiro Game_State
currentGameState = gameOverMenu.execute_menu()

globalGameExit = False
while not globalGameExit:
   if currentGameState == Representations.gameStates["ON_START_MENU"]:
       currentGameState = startMenu.execute_menu()
   elif currentGameState == Representations.gameStates["PLAYING"]:
       currentGameState = currentLevel.execute_level()
   elif currentGameState == Representations.gameStates["GOING_TO_NEXT_LEVEL"]:
       currentGameState = currentLevel.execute_level()
   elif currentGameState == Representations.gameStates["GAME_OVER"]:
       currentGameState = gameOverMenu.execute_menu()
   elif currentGameState == Representations.gameStates["ON_INSTRUCTIONS"]:
       currentGameState = openingInstructions.execute_instructions()

pygame.quit()
quit()
