from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, coord, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            join("..", "Assets", "Images", "Idle_Leaf", "Leaf_Idle_Animation1.png")
        ).convert_alpha()
        self.rect = self.image.get_frect(center=coord)
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = 300

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        if int(keys[pygame.K_SPACE]):
            pass  # implement jumping once player can move

    def move(self, dt):
        self.rect.center += self.direction * VELOCITY * dt

    def update(self, dt):
        self.get_input()
        self.move(dt)

    def get_coords(self):
        return (self.rect.centerx, self.rect.centery)
