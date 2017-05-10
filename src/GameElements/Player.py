import math
import pygame
from src import Representations

playerColor = (255, 0, 0)


playerRadius = 10
stepSize = 5.0

class Player:
    # This class is resposible for the main character, the player of the game
    def __init__(self, path):
        self.gameSurface = pygame.display.get_surface()
        self.path = path
        self.xPos = Representations.xInitialPos
        self.yPos = self.gameSurface.get_height() / 2
        self.cowboy1 = pygame.image.load("src/Assets/Images/CowboySprites/cowboy_1.png")
        self.cowboy2 = pygame.image.load("src/Assets/Images/CowboySprites/cowboy_2.png")

    def draw(self,counter):
    # plots the player in the display
        self.playerPos= (self.xPos,self.yPos)
        decade = round(counter/10.0)
        if decade%2 == 0:
            self.gameSurface.blit(self.cowboy1, (self.xPos,self.yPos -60))
        else:
            self.gameSurface.blit(self.cowboy2, (self.xPos, self.yPos -60 ))

    def step(self):
    # player is one step closer to the end of the game
        self.xPos += stepSize
        levelLength = 0.7 * self.gameSurface.get_width() / (self.path.numberOfLevels + 1)
        if self.xPos > (levelLength + Representations.xInitialPos): # In this case yPos changes
            levelHeight = 0.8 * self.gameSurface.get_height() / self.path.numberOfLevels
            tangent = levelHeight / (2 * levelLength)

            xFork = math.floor((self.xPos - Representations.xInitialPos) / (levelLength))
            # yFork = (xFork - 1) 8- math.floor((self.yPos - (display_height/2)) / (levelHeight / 2))
            forkNumber = 2 ** (xFork - 1)
            forkNumber += (xFork - 1) + math.floor((self.yPos - (self.gameSurface.get_height()/2)) / (levelHeight))

            if (self.xPos - Representations.xInitialPos) / (levelLength) - math.floor((self.xPos - Representations.xInitialPos) / (levelLength)) == 0:
                xFork = math.floor((self.xPos - stepSize - Representations.xInitialPos) / (levelLength))
                # yFork = (xFork - 1) - math.floor((self.yPos - (display_height/2)) / (levelHeight / 2))
                forkNumber += (xFork - 1) + math.floor((self.yPos - (self.gameSurface.get_height() / 2)) / (levelHeight))

            nextFork = self.path.forkTree[forkNumber]

            if nextFork.forkState == Representations.forkState["UP"]: # Fork is up
                self.yPos += tangent * stepSize
            elif nextFork.forkState == Representations.forkState["DOWN"]: # Fork is down
                self.yPos -= tangent * stepSize


    def toggle(self):
    # toggles the next forks of the path
        levelLength = 0.7 * self.gameSurface.get_width() / (self.path.numberOfLevels + 1)
        xFork = math.floor((self.xPos - Representations.xInitialPos) / (levelLength))

        if xFork < self.path.numberOfLevels:
            levelLength = 0.7 * self.gameSurface.get_width() / (self.path.numberOfLevels + 1)
            level = math.floor((self.xPos - Representations.xInitialPos) / levelLength)
            firstFork = 2 ** level
            if level < self.path.numberOfLevels:
                for i in range(firstFork, 2 * firstFork):
                    self.path.forkTree[i].toggle()

    def pathConcluded(self):
        if self.xPos >= Representations.xInitialPos + 0.7 * self.gameSurface.get_width() - (4 * stepSize):
            return True
        return False

    def didWin(self):
        if self.pathConcluded() == False:
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