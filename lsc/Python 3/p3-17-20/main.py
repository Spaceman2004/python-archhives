from pygame import *

init()
my_vec = math.Vector2
HEIGHT = 420
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

framsper = time.Clock()
disp_srf = display.set_mode(WIDTH, HEIGHT)
display.set_caption('Platformer')


class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = Surface((30, 40))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))


class Platform(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = Surface((WIDTH, 20))
        self.surf.fill((0xff, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))


PT1 = Platform()  # Platform
PL1 = Player()    # Player

all_sprites = sprite.Group()
all_sprites.add(PT1)
all_sprites.add(PL1)

platforms = sprite.Group()
