from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = self.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Autumn Explorer")
        self.clock = pygame.time.Clock()
        self.play = True

    def run(self):
        while self.play:
            # Frame rate:
            dt = self.clock.tick(FRAME_RATE) / 1000

            # Events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            # update

            # draw
            pygame.display.update()

        pygame.quit()


game = Game()
game.run()
