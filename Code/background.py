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

    def background_move(self, dt):
        if self.pos > 0 and self.direction < 0:
            self.pos += self.direction * VELOCITY * dt
        if self.pos < 5000 and self.direction > 0:
            self.pos += self.direction * VELOCITY * dt

    def background_display(self, screen):
        for dist in range(5):
            speed = 1
            for layer in self.layers:
                screen.blit(layer, ((dist * self.width) - (self.pos * speed), 0))
                speed += 0.2

    def update(self, screen, dt):
        self.get_input()
        self.background_move(dt)
        self.background_display(screen)
