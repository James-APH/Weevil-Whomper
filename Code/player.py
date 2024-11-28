from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, z_coord, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("../images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center=(WIDTH / 2, HEIGHT / 2 - 100))
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = 300
