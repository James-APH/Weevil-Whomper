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
        self.moving = Movement
        self.sprite_move_value = 0

    def animate(self):
        pass

    def get_input(self):
        keys = pygame.key.get_pressed()
        # Setting enum for character animation
        if keys[pygame.K_RIGHT]:
            self.moving = Movement.RIGHT
        if keys[pygame.K_LEFT]:
            self.moving = Movement.LEFT
        # Moving Object
        if self.moving == Movement.LEFT or self.moving == Movement.RIGHT:
            self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        else:
            self.moving = Movement.IDLE

    def move(self, dt):
        if (self.rect.left + (self.direction[0] * VELOCITY * dt) < BOUNDARY / 2) or (
            self.rect.right + (self.direction[0] * VELOCITY * dt) > WIDTH - BOUNDARY / 2
        ):
            pass
        else:
            self.rect.center += self.direction * VELOCITY * dt

    def update(self, dt):
        self.get_input()
        self.move(dt)
        self.animate()

    def get_coords(self):
        return (self.rect.centerx, self.rect.centery)
