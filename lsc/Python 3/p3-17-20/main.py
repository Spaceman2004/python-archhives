from pygame import *

init()
my_vec = math.Vector2
HEIGHT = 450
WIDTH = 420
ACC = 0.5
FRIC = -0.12
FPS = 60

framsper = time.Clock()
disp_srf = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Platformer')


class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = Surface((30, 40))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(20, 410))
        self.pos = my_vec((10, 385))
        self.vel = my_vec(0, 0)


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
platforms.add(PT1)

while True:
    for evnt in event.get():
        if evnt.type == QUIT:
            quit()
    disp_srf.fill((0, 0, 0))

    for entity in all_sprites:
        disp_srf.blit(entity.surf, entity.rect)

    display.update()
    framsper.tick(FPS)