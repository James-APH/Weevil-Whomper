from settings import *


class Button(pygame.sprite.Sprite):
    def __init__(self, coord, button_type, groups):
        super().__init__(groups)
        self.path = join("..", "Assets", "Images", "Buttons")
        self.images = {"Play": [], "Quit": []}
        self.load_images()
        self.button_type = button_type

        if button_type == "Play":
            self.image = pygame.image.load(
                join("..", "Assets", "Images", "Buttons", "Play", "Play_Button_1.png")
            ).convert_alpha()
        else:
            self.image = pygame.image.load(
                join("..", "Assets", "Images", "Buttons", "Quit", "Quit_Button_1.png")
            ).convert_alpha()

        self.button_state = Button_State.NONE
        self.sprite_index = 0
        self.rect = self.image.get_frect(center=coord)
        self.width = self.image.get_width()
        self.state_rate = 2

    def load_images(self):
        for path, sub_dirs, files in walk(self.path):
            for dir in sub_dirs:
                for file_name in sorted(listdir(join(path, dir))):
                    image = pygame.image.load(
                        join(path, dir, file_name)
                    ).convert_alpha()
                    self.images[dir].append(image)

    def get_input(self) -> bool:
        # update value of self.button_state
        keys = pygame.key.get_pressed()
        mouse_position = pygame.mouse.get_pos()
        # getting mouse location:
        if (
            mouse_position[0] > self.rect.left
            and mouse_position[0] < self.rect.right
            and mouse_position[1] > self.rect.top
            and mouse_position[1] < self.rect.bottom
        ):
            if sum(pygame.mouse.get_pressed()) > 0:
                self.button_state = Button_State.PRESSED
                return True
        return False

    def animate(self, dt):
        if self.button_state == Button_State.PRESSED:
            self.sprite_index += self.state_rate * dt
            self.image = self.images[self.button_type][
                int(self.sprite_index) % len(self.images[self.button_type])
            ]

    def button_display(self, screen, dt):
        for _ in range(4):
            self.animate(dt)
            screen.blit(self.image, self.rect)

    def update(self, screen, dt):
        self.get_input()
        self.button_display(screen, dt)
