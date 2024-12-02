from settings import *


class Background(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.layers = []
        for i in range(1, 7):
            self.layers.append(
                pygame.image.load(
                    join(
                        "..",
                        "Assets",
                        "Images",
                        "Background",
                        f"Autumn Background - {i}.png",
                    )
                ).convert_alpha()
            )
        self.width = self.layers[0].get_width()
        self.direction = 0
        self.pos = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])

    def background_move(self, player_pos, dt):
        move_space = BOUNDARY * 2
        if player_pos < move_space or player_pos > WIDTH - move_space:
            if self.pos > 0 and self.direction < 0 and player_pos < WIDTH / 2:
                self.pos += self.direction * VELOCITY * dt
            if self.pos < 10000 and self.direction > 0 and player_pos > WIDTH / 2:
                self.pos += self.direction * VELOCITY * dt

    def background_display(self, screen):
        for dist in range(5):
            velocity = 1
            for layer in self.layers:
                screen.blit(layer, ((dist * self.width) - (self.pos * velocity), 0))
                velocity += 0.1

    def update(self, screen, player_pos, dt):
        self.get_input()
        self.background_move(player_pos, dt)
        self.background_display(screen)
