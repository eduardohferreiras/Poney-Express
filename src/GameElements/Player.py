import math
import pygame
from src import Representations

playerColor = (255, 0, 0)


playerRadius = 10
stepSize = 5.0

class Player:
    # This class is resposible for the main character, the player of the game
    # It has to implement the step of the player so it can ran on a way of the path
    # It also implements the toggle which changes the next possible Forks
    def __init__(self, path):
        self.gameSurface = pygame.display.get_surface()
        self.path = path # It receives the path it is going to walk on
        self.xPos = Representations.xInitialPos
        self.yPos = self.gameSurface.get_height() / 2
        self.cowboy1 = pygame.image.load("src/Assets/Images/CowboySprites/cowboy_1.png")
        self.cowboy2 = pygame.image.load("src/Assets/Images/CowboySprites/cowboy_2.png")

        # We need to toggle twice for a smoother game experience
        for fork in self.path.forkTree:
            fork.toggle()
            fork.toggle()

    def draw(self,counter):
        # plots the player in the display
        self.playerPos= (self.xPos,self.yPos)
        decade = round(counter/10.0)
        # It gives the sense of motion of the player (cowboy) as it is running
        if decade%2 == 0:
            self.gameSurface.blit(self.cowboy1, (self.xPos,self.yPos -60)) # Position 1 of the moviment of running
        else:
            self.gameSurface.blit(self.cowboy2, (self.xPos, self.yPos -60 )) # Position 2 of the moviment of running

    def step(self):
        # Player is one step closer to the end of the game
        # Each step is rendered on screen as a new frame
        self.xPos += stepSize # Advances in the x axis

        levelLength = 0.8 * self.gameSurface.get_width() / (self.path.numberOfLevels + 1)
        if self.xPos > (levelLength + Representations.xInitialPos): # If it is not in the initial straight line then it also
                                                                    # moves up or down depending on the Fork orientation
            levelHeight = 0.8 * self.gameSurface.get_height() / self.path.numberOfLevels
            tangent = levelHeight / (2 * levelLength) # Tangent of the inclination of the path
            xFork = math.floor((self.xPos - Representations.xInitialPos) / (levelLength))
            forkIndex = 2 ** (xFork-1)
            currentFork = self.path.forkTree[forkIndex]
            print(currentFork.forkState)
            if currentFork.forkState == Representations.forkState["UP"]: # Fork is up
                self.yPos -= tangent * stepSize
            elif currentFork.forkState == Representations.forkState["DOWN"]: # Fork is down
                self.yPos += tangent * stepSize


    def toggle(self):
        # toggles the next forks of the path
        levelLength = 0.8 * self.gameSurface.get_width() / (self.path.numberOfLevels + 1)
        xFork = math.floor((self.xPos - Representations.xInitialPos) / (levelLength))

        if xFork < self.path.numberOfLevels:
            levelLength = 0.8 * self.gameSurface.get_width() / (self.path.numberOfLevels + 1)
            level = math.floor((self.xPos - Representations.xInitialPos) / levelLength)
            firstFork = 2 ** level
            # All the forks of the next level are changed
            if level < self.path.numberOfLevels:
                for i in range(firstFork, 2 * firstFork):
                    if i < len(self.path.forkTree):
                        self.path.forkTree[i].toggle()

    def pathConcluded(self):
        # Returns if the player got to the end of the path
        if self.xPos >= Representations.xInitialPos + 0.8 * self.gameSurface.get_width() - (4 * stepSize):
            return True
        return False

    def didWin(self):
        # Returns if the player got to the right exit of the path
        if self.pathConcluded() == False: # If player didnt reach the end, it cant return
            pass
        elif self.pathConcluded() == True:
            levelHeight = 0.8 * self.gameSurface.get_height() / self.path.numberOfLevels
            yTarget = self.gameSurface.get_height() / 2
            if self.path.numberOfExits%2 == 0:
                yTarget += ((self.path.rightExit - (self.path.numberOfExits/2)) * levelHeight) + (levelHeight/2)
            elif self.path.numberOfExits%2 == 1:
                yTarget += (self.path.rightExit - math.floor(self.path.numberOfExits/2)) * levelHeight

            if (self.yPos < yTarget + (levelHeight/2)) and (self.yPos > yTarget - (levelHeight/2)):
                return True
            return False