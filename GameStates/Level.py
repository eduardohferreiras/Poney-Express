import pygame, Representations
from GameElements import Path, Player

pygame.init()

class Level():
    def __init__(self):
        self.isPlaying = True
        self.difficulty = 1
        self.path = None
        self.player = None

    def set_background_image(self, file):
        self.backgroundImage = pygame.image.load(file)

    def play_music(self, file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1, 0)

    def execute_level(self):

        self.set_background_image('Assets/Images/Phase_1.jpg')
        path = Path.Path(self.difficulty)
        player = Player.Player(path)
        gameCanvas = pygame.display.get_surface()

        clock = pygame.time.Clock()
        while self.isPlaying:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isPlaying = False
                    return Representations.gameStates["SHUTTING DOWN"]
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
                        return Representations.gameStates["SHUTTING DOWN"]

            if player.pathConcluded():
                if player.didWin():
                    self.difficulty = self.difficulty + 1
                    return Representations.gameStates["GOING_TO_NEXT_LEVEL"]
                elif not player.didWin():
                    return Representations.gameStates["GAME_OVER"]
            elif not player.pathConluded():
                #Ver se clicou, dar step, atualizar tudo, dar display.update(), blit?.
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP
                        player.toggle()

                player.step()
                gameCanvas.blit(self.backgroundImage, (0,0))
                player.draw()
                path.plotPath()
                pygame.display.update()
                clock.tick(60)