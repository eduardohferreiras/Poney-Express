import pygame

from src import Representations
from src.GameElements import Canvas
from src.GameStates import Level, Start_Menu, Game_Over_Menu, Opening_Instructions

pygame.init()

#Inicialization of instanece of some classes
canvas = Canvas.Canvas(1080, 1920) #canvas is the display of the game. Here, we set the game resolution to Full HD.
currentLevel = Level.Level() #curentLevel is the class that represents a level of the game. It's main responsibilities are to set up the path and get the user clicks and.
openingInstructions = Opening_Instructions.Opening_Instructions() #openingInstruction is the initial apresentation of the game plot and mechanics.
startMenu = Start_Menu.Start_Menu() #startMenu is the class that controls the start menu.
gameOverMenu = Game_Over_Menu.Game_Over_Menu() # gameOverMenu is the class that controls the game over menu/screen.

# Setting the game canvas.
canvas.set_canvas()


#Here, we use a State Machine to control which state of the game is being executed.

globalGameExit = False #currentGameState contains the information about the current game mode.
currentGameState = startMenu.execute_menu()#currentGameState contains the information about the current game mode.
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
   elif currentGameState == Representations.gameStates["SHUTTING DOWN"]:
       globalGameExit = True

pygame.quit()
quit()
