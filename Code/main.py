from settings import *
from player import Player
from background import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Autumn Explorer")
        self.clock = pygame.time.Clock()
        self.play = True

        # Sprite Groups
        self.main_sprites = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()
        self.player = Player((WIDTH / 2, HEIGHT / 2), self.main_sprites)
        self.background = Background(self.background_sprites)

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
            self.background.draw(self.screen)
            self.main_sprites.update(dt)
            self.main_sprites.draw(self.screen)
            pygame.display.update()

        pygame.quit()


game = Game()
game.run()
