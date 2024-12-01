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

    def draw(self, screen):
        for layer in self.layers:
            screen.blit(layer, (0, 0))

    def update(self, dt):
        pass
