import pygame
from src import Representations
from pygame.locals import *

pygame.init()

display_width = 1920
display_height = 1080

color = (255,255,255)

class Opening_Instructions:

    def __init__(self):
        self.isInsideInstructions = True
        self.instructionsState = 0

    #Function created to help "message_to_screen" in printing messages in the right place (center of the screen),
    #with the aid of rectangles
    def text_objects(self, text):
        textSurface = self.font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    #Defines the function to print message to screen
    def message_to_screen(self, msg, delta_y):
        textSurface, textRect = self.text_objects(msg)
        textRect.center = (display_width / 2), ((display_height / 2) + delta_y)
        self.gameCanvas.blit(textSurface, textRect)

    #Assigns background image of the Instructions game state
    def set_background_image(self, file):
        self.backgroundImage = pygame.image.load(file)

    #Assigns font obtained from file to be used when printing messages to the user
    def set_font(self, file, size):
        self.font = pygame.font.Font(file, size)

    #Only responsible for the mixing of the soundtrack
    @staticmethod
    def play_music(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1, 0)

    #First set of dialog box printed to the user
    def set1(self):
        self.message_to_screen("""Howdy partner!""", 0)
        self.message_to_screen("""My name is Ben Cartwright, and I'm one of The Pony Express Riders of Iowa""", 40)
        self.message_to_screen("""Our intention is to get all the gold in the West""", 80)
        self.message_to_screen("""For that we need only the bravest and most skilled cowboys among us""", 120)
        self.message_to_screen("""And that's why we seekin' you!""", 160)

    #Second set of dialog box that is printed to the user
    def set2(self):
        self.message_to_screen("""Now be careful, boy! This is dangerous business...""", 0)
        self.message_to_screen("""Sheriffs don't like we hangin' around, stealin' all this gold... They want us dead!""", 40)
        self.message_to_screen("""So they started makin' a trap for all of us: instead of gold, there will be roads with bombs and dynamite!""", 80)
        self.message_to_screen("""They want us dead""", 120)

    #Third and last set of dialog box printed to the user
    def set3(self):
        self.message_to_screen("""But we ain't called The Riders for no reason: we got some special skills in our side:""", 0)
        self.message_to_screen("""Every time you are in a road and face a fork facing North, you can switch it to make it face South, and vice-versa""", 40)
        self.message_to_screen("""That said, in order to get to the good gold we want, we need to keep switching the forks in our way by pressing the SPACEBAR""", 80)
        self.message_to_screen("""Oh! And watch out on this: in every fork, you will find two roads, a light-brown one, and a dark-brown one:""", 120)
        self.message_to_screen("""You will always run through the light-brown one. That is, you will toggle the forks so that the light-brown road leads to the direction you intended to go.""", 160)
        self.message_to_screen("""Enough talkin'! Off to the gold!""", 200)

    #Main function, used to activate all the rest of the class Opening_Instructions, in the right order
    def execute_instructions(self):
        self.set_background_image('src/Assets/Images/CowboyInstructor.jpg')
        self.set_font("src/Assets/Fonts/BillytheKid.ttf", 40)
        self.gameCanvas = pygame.display.get_surface()

        self.gameCanvas.blit(self.backgroundImage, (0, 0))
        self.set1()
        self.instructionsState = 1
        clock = pygame.time.Clock()

        #Main Loop, responsible for printing the right set of dialogs to the user, and configuring its appearance
        while self.isInsideInstructions:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isInsideInstructions = False
                    return Representations.gameStates["SHUTTING DOWN"]
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
                        return Representations.gameStates["SHUTTING DOWN"]
                    elif event.type == K_SPACE:
                        if self.instructionsState == 1:
                            self.gameCanvas.blit(self.backgroundImage, (0, 0))
                            self.set2()
                            self.instructionsState = 2
                        elif self.instructionsState == 2:
                            self.gameCanvas.blit(self.backgroundImage, (0, 0))
                            self.set3()
                            self.instructionsState = 3
                        else:
                            self.isInsideInstructions = False
                            return Representations.gameStates["PLAYING"]
                pygame.display.update()
                clock.tick(60)

