from settings import *


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
        self.update_val = 2

    def load_images(self):
        for path, sub_dirs, files in walk(self.path):
            for dir in sub_dirs:
                for file_name in sorted(listdir(join(path, dir))):
                    image = pygame.image.load(
                        join(path, dir, file_name)
                    ).convert_alpha()
                    self.images[dir].append(image)

    def animate(self, dt):
        self.sprite_index += self.update_val * dt
        if self.movement == Movement.LEFT:
            self.image = self.images[Movement.LEFT][
                int(self.sprite_index) % len(self.images[Movement.LEFT])
            ]
            self.update_val = 4
        if self.movement == Movement.RIGHT:
            self.image = self.images[Movement.RIGHT][
                int(self.sprite_index) % len(self.images[Movement.RIGHT])
            ]
            self.update_val = 4
        if self.movement == Movement.IDLE:
            self.image = self.images[Movement.IDLE][
                int(self.sprite_index) % len(self.images[Movement.IDLE])
            ]
            self.update_val = 2

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            if keys[pygame.K_RIGHT]:
                if self.movement != Movement.RIGHT:
                    self.sprite_index = 0
                self.movement = Movement.RIGHT
            elif keys[pygame.K_LEFT]:
                if self.movement != Movement.LEFT:
                    self.sprite_index = 0
                self.movement = Movement.LEFT
        else:
            if self.movement != Movement.IDLE:
                self.sprite_index = 0
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
        self.animate(dt)
        self.move(dt)

    def get_coords(self):
        return (self.rect.centerx, self.rect.centery)
