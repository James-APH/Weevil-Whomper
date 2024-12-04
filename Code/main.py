from settings import *
from player import Player
from background import Background
from Splash import SplashScreen


# New idea: just check where the players x-coord is, and if the x-coord > 9999 then end the game
# can still have buttons.

# can think about adding a message at the beginning


class Game:
    def __init__(self):
        pygame.init()

        # Base Settings
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Autumn Explorer")
        self.clock = pygame.time.Clock()
        self.play = True

        # Sprite Groups
        self.main_sprites = pygame.sprite.Group()
        self.background_sprites = pygame.sprite.Group()
        self.splash_sprites = pygame.sprite.Group()
        # Objects
        self.splash_screen = SplashScreen(self.splash_sprites)
        self.player = Player((WIDTH / 2, HEIGHT - 128), self.main_sprites)
        self.background = Background(self.background_sprites)
        self.splash_state = Splash.TITLE

    def run(self):
        while self.play:
            # Frame rate:
            dt = self.clock.tick(FRAME_RATE) / 1000
            # Events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            if self.splash_state == Splash.TITLE:
                self.splash_screen.update(self.screen, self.splash_state)

            # Updating player and background positions
            else:
                self.background.update(self.screen, self.player.get_coords()[0], dt)
                self.main_sprites.update(dt)
                self.main_sprites.draw(self.screen)
                pygame.display.update()

        pygame.quit()


game = Game()

game.run()
