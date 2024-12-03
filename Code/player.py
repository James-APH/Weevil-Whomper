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

        # loading images
        self.idle_images = []
        self.left_images = []
        self.right_images = []
        self.load_images()

    def load_images(self):
        self.idle_images = []
        for i in range(1, 12):
            self.idle_images.append(
                pygame.image.load(
                    join(
                        "..",
                        "Assets",
                        "Images",
                        "Idle_Leaf",
                        f"Leaf_Idle_{i}.png",
                    )
                ).convert_alpha()
            )

        self.right_images = []
        for i in range(1, 9):
            self.right_images.append(
                pygame.image.load(
                    join(
                        "..",
                        "Assets",
                        "Images",
                        "Right_Walk_Leaf",
                        f"Leaf_Right_{i}.png",
                    )
                ).convert_alpha()
            )

        # LEFT
        self.left_images = []
        for i in range(1, 9):
            self.left_images.append(
                pygame.image.load(
                    join(
                        "..",
                        "Assets",
                        "Images",
                        "Left_Walk_Leaf",
                        f"Leaf_Left_{i}.png",
                    )
                ).convert_alpha()
            )

    def animate(self):
        # need to implement this kinda like a state machine
        # it will need to update each time the function is called
        image_lis = []
        sprite_limit = 0
        if self.moving == Movement.LEFT:
            pass
        if self.moving == Movement.RIGHT:
            pass
        if self.moving == Movement.IDLE:
            pass

    def get_input(self):
        keys = pygame.key.get_pressed()
        # Setting enum for character animation
        if keys[pygame.K_RIGHT]:
            if self.moving == Movement.LEFT:
                self.sprite_move_value = 0
            self.moving = Movement.RIGHT
        if keys[pygame.K_LEFT]:
            if self.moving == Movement.RIGHT:
                self.sprite_move_value = 0
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
