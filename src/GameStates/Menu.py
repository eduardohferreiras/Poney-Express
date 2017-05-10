import pygame

class Menu():
    def __init__(self):
        self.isInMenu = True

    def set_background_image(self, file):
        self.backgroundImage = pygame.image.load(file)

    def play_music(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

    def text_objects(self, text, font, RGBcolor):
        textSurface = font.render(text, True, RGBcolor)
        return textSurface, textSurface.get_rect()

    def execute_menu(self):
        pass