from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, coord, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            join("..", "Assets", "Images", "Idle_Leaf", "Leaf_Idle_Animation1.png")
        ).convert_alpha()
        self.rect = self.image.get_frect(center=coord)
        self.direction = pygame.math.Vector2(0, 0)
        self.width = self.image.get_width()

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        if int(keys[pygame.K_SPACE]):
            pass  # implement jumping once player can move

    def move(self, dt):
        if (
            self.rect.left + (self.direction[0] * VELOCITY * dt) < 0 + self.width / 2
        ) or (
            self.rect.right + (self.direction[0] * VELOCITY * dt)
            > WIDTH - self.width / 2
        ):
            pass
        else:
            self.rect.center += self.direction * VELOCITY * dt

    # $  and (self.rect.centerx + (self.direction[0] * VELOCITY * dt))
    # ) < WIDTH - self.width:
    #   self.rect.center += self.direction * VELOCITY * dt

    def update(self, dt):
        self.get_input()
        self.move(dt)

    def get_coords(self):
        return (self.rect.centerx, self.rect.centery)
