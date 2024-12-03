from settings import *
from os import walk
from os import listdir


class Player(pygame.sprite.Sprite):
    def __init__(self, coord, groups):
        super().__init__(groups)
        self.path = join("..", "Assets", "Images", "Player")
        self.images = {"Idle_Leaf": [], "Right_Walk_Leaf": [], "Left_Walk_Leaf": []}
        self.load_images()

        self.image = pygame.image.load(
            join("..", "Assets", "Images", "Player", "Idle_Leaf", "Leaf_Idle_1.png")
        ).convert_alpha()
        self.movement = Movement.IDLE
        self.sprite_index = 0

        self.rect = self.image.get_frect(center=coord)
        self.direction = pygame.math.Vector2(0, 0)
        self.width = self.image.get_width()

    def load_images(self):
        for path, sub_dirs, files in walk(self.path):
            for dir in sub_dirs:
                for file_name in sorted(listdir(join(path, dir))):
                    image = pygame.image.load(
                        join(path, dir, file_name)
                    ).convert_alpha()
                    self.images[dir].append(image)

    def animate(self, dt):
        self.sprite_index += 5 * dt
        if self.movement == Movement.LEFT:
            self.image = self.images[Movement.LEFT][
                int(self.sprite_index) % len(self.images[Movement.LEFT])
            ]
        if self.movement == Movement.RIGHT:
            self.image = self.images[Movement.RIGHT][
                int(self.sprite_index) % len(self.images[Movement.RIGHT])
            ]
        if self.movement == Movement.IDLE:
            self.image = self.images[Movement.IDLE][
                int(self.sprite_index) % len(self.images[Movement.IDLE])
            ]

    def get_input(self):
        keys = pygame.key.get_pressed()
        # Setting enum for character animation and preventing movement overlap
        if keys[pygame.K_RIGHT]:
            if self.movement == Movement.LEFT:
                self.sprite_move_value = 0
            self.movement = Movement.RIGHT
        if keys[pygame.K_LEFT]:
            if self.movement == Movement.RIGHT:
                self.sprite_move_value = 0
            self.movement = Movement.LEFT
        # movement Object
        if self.movement == Movement.LEFT or self.movement == Movement.RIGHT:
            self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        else:
            self.movement = Movement.IDLE

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
        self.animate(dt)

    def get_coords(self):
        return (self.rect.centerx, self.rect.centery)
