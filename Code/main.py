from settings import *
from player import Player
from background import Background
from Splash import SplashScreen
from Button import Button

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
        self.button_sprites = pygame.sprite.Group()
        # Objects
        self.play_button = Button(
            ((WIDTH / 2) - (WIDTH / 4), (HEIGHT / 3) * 2), "Play", self.button_sprites
        )
        self.quit_button = Button(
            ((WIDTH / 2) + (WIDTH / 4), (HEIGHT / 3) * 2), "Quit", self.button_sprites
        )
        self.splash_screen = SplashScreen(self.splash_sprites)
        self.player = Player((WIDTH / 2, HEIGHT - 128), self.main_sprites)
        self.background = Background(self.background_sprites)
        self.splash_state = Splash.TITLE

    def title(self):
        while self.splash_state != Splash.NONE:

            dt = self.clock.tick(FRAME_RATE) / 1000
            # Events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            self.screen.blit(self.splash_screen.get_splash(self.splash_state))
            self.play_button.update(self.screen, dt)
            self.quit_button.update(self.screen, dt)
            if self.play_button.get_input():
                self.splash_state = Splash.NONE
                self.run_game()
            elif self.quit_button.get_input():
                self.splash_state = Splash.NONE
                pygame.quit()

            pygame.display.update()

    def win(self):
        while self.splash_state != Splash.NONE:

            dt = self.clock.tick(FRAME_RATE) / 1000
            # Events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            self.screen.blit(self.splash_screen.get_splash(self.splash_state))
            self.play_button.update(self.screen, dt)
            self.quit_button.update(self.screen, dt)
            if self.play_button.get_input():
                self.splash_state = Splash.NONE
                self.run_game()
            elif self.quit_button.get_input():
                self.splash_state = Splash.NONE
                pygame.quit()

            pygame.display.update()

    def run_game(self):
        while self.play:
            # Frame rate:
            dt = self.clock.tick(FRAME_RATE) / 1000
            # Events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            if self.player.get_coords()[0] >= 5000:
                self.splash_state = Splash.WIN
                self.win()

            # Updating player and background positions
            self.background.update(self.screen, self.player.get_coords()[0], dt)
            self.main_sprites.update(dt)
            self.main_sprites.draw(self.screen)
            pygame.display.update()

        pygame.quit()


game = Game()

game.title()
