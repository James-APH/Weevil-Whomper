from settings import *


class SplashScreen(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.path = join("..", "Assets", "Images", "Splash")
        self.images = {}
        self.load_images()

    def load_images(self):
        for path, sub_dirs, files in walk(self.path):
            for file in files:
                file_name = file.replace(".png", "")
                image = pygame.image.load(join(path, file)).convert_alpha()
                print(f"dir: {file_name}, file w/ path: {image}")
                self.images[file_name] = image

    def get_splash(self, splash_type):
        return self.images[splash_type]
