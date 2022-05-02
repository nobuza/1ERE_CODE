import pygame
import random

# --- constants --- (UPPER_CASE names)

WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
ORANGE = (255, 255,   0)
YELLOW = (  0, 255, 255)

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

FPS = 60

# --- classes --- (CamelCase names)

class Player(pygame.sprite.Sprite):
                                     # <-- empty line for readabelity
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("../assets/sprites/frisk.png").convert()
        self.rect = self.image.get_rect()
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x

# --- functions --- (lower_case names)

# empty

# --- main --- (lower_case names)

# - init -

pygame.init()
pygame.mixer.init()

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
display_rect = display.get_rect()

# - objects -

all_sprites = pygame.sprite.Group()

player = Player()
player.rect.center = display_rect.center
player.speed_x = 1

all_sprites.add(player)

background = pygame.image.load("../assets/sprites/trueLab.png").convert()
background = pygame.transform.scale(background, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

# - other -

pygame.mixer.music.load("../assets/OST/here-we-are.mp3")
pygame.mixer.music.play(-1)

# - mainloop -

crashed = False
clock = pygame.time.Clock()

while not crashed:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    # - updates (without draws) -

    all_sprites.update()

    # - draws (without updates) -

    display.blit(background, (0, 0))

    all_sprites.draw(display)

    pygame.display.update()

    # - FPS -

    clock.tick(FPS)

# - end -
pygame.quit()