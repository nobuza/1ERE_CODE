# Libs Python --------------------------------------------------------------- #
from numpy import disp
import pygame, sys, math, random, os
from button import Button


# Inits Python --------------------------------------------------------------- #
pygame.init()
pygame.mixer.init()


# Setup Pygame/window -------------------------------------------------------- #
pygame.display.set_caption("Touhou 19: The return of Neco Arc")
clock = pygame.time.Clock()
FPS = 60

window_width = 1152
window_height = 864

SCREEN = pygame.display.set_mode((window_width, window_height))

field = pygame.Rect(window_width/32, window_height/64, window_width/2, (window_height - window_height/16))

# Setup Animations/Display/Sprites ----------------------------------------------------------- #
curDir = os.path.dirname(os.path.realpath(__file__)) + '/'
img_path = 'data/images/'
ost_path = 'data/ost/'
font_path = 'data/fonts/'

yellow_bullet_img = pygame.image.load(curDir + img_path + 'projectiles/yellow_bullet/yellow_bullet.png')
red_bullet_img = pygame.image.load(curDir + img_path + 'projectiles/red_bullet/red_bullet.png')

menu_bg_img = pygame.image.load(curDir + img_path + 'backgrounds/MAIN_MENU_BG_V2.png')
menu_bg_img = pygame.transform.scale(menu_bg_img, (1152, 864))

skies_of_gensokyo_img = pygame.image.load(curDir + img_path + 'backgrounds/skies_of_gensokyo.jpg')
skies_of_gensokyo_img = pygame.transform.scale(skies_of_gensokyo_img, (1152, 864))

awoo_img = pygame.image.load(curDir + img_path + 'backgrounds/awoo.jpg')
awoo_img = pygame.transform.scale(awoo_img, (1152, 864))

reimu_sp_2_img = pygame.image.load(curDir + img_path + 'entities/reimu/reimu_sp_2.png')
reimu_sp_2_img = pygame.transform.scale(reimu_sp_2_img, (40, 60))

nazrin_sp_1_img = pygame.image.load(curDir + img_path + 'entities/nazrin/nazrin_sp_1.png')
nazrin_sp_1_img = pygame.transform.scale(nazrin_sp_1_img, (60, 80))

button_rect_1 = pygame.image.load(curDir + img_path + 'rects/button_rect_1.png')
button_rect_1 = pygame.transform.scale(button_rect_1, (250, 70))

button_rect_2 = pygame.image.load(curDir + img_path + 'rects/button_rect_2.png')
button_rect_2 = pygame.transform.scale(button_rect_2, (225, 50))

all_sprites = pygame.sprite.Group()

SCREEN_RECT = SCREEN.get_rect()


# Setup Entities and Objects ------------------------------------------------- #
start_localizations = {'reimu': [int(field.x + field.width/2.2), int(field.y + field.height/1.2)], 'nazrin': [int(field.x + field.width/2.2), int(field.y + field.height*3/16)]}

projectiles = []
projectile_rects = []
seeking_projectiles = []
elementsOnScreen = []


# Pygame audio mixer pre-loading ------------------------------------------------- #
menu_theme = pygame.mixer.Sound(curDir + ost_path + 'menu_theme.mp3')
ost_channel = pygame.mixer.Channel(1)
ost_channel.play(menu_theme)

# Functions ----------------------------------------
def get_border_rects(inner_rect, outer_rect):
    inner, outer = inner_rect, outer_rect # for shortening
    l_rect = pygame.Rect(outer.x, outer.y, (inner.x - outer.x), outer.height)
    r_rect = pygame.Rect(inner.right, outer.y, (outer.right - inner.right), outer.height)
    t_rect = pygame.Rect(outer.x, outer.y, outer.width, (inner.y - outer.y))
    b_rect = pygame.Rect(outer.x, inner.bottom, outer.width, (outer.bottom - inner.bottom))
    return [l_rect, r_rect, t_rect, b_rect]

def get_font_watatsuki(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(curDir + font_path + 'WatatsukiTechSans.ttf', size)

def get_font_yuki_boku(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(curDir + font_path + 'YujiBoku-Regular.ttf', size)

# Classes ------------------------------------------
class Reimu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #----------------------
        # Basic init stuff
        pygame.sprite.Sprite.__init__(self)
        self.image = reimu_sp_2_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.x = int(start_localizations['reimu'][0])
        self.y = int(start_localizations['reimu'][1])
        

        #----------------------
        #Movement system utilities
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

        #----------------------
        #Collision system utilities
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def update(self):
        #----------------------
        #Movement system utilities
        self.vel_x = 0
        self.vel_y = 0
        global reimu_velocity
        reimu_velocity = (self.vel_x, self.vel_y)
        speed_diviser_value = 2
        if self.left_pressed and not self.right_pressed:
            self.vel_x = -self.speed / speed_diviser_value
        if self.right_pressed and not self.left_pressed:
            self.vel_x = self.speed / speed_diviser_value
        if self.up_pressed and not self.down_pressed:
            self.vel_y = -self.speed / speed_diviser_value
        if self.down_pressed and not self.up_pressed:
            self.vel_y = self.speed / speed_diviser_value
        
        border_rects = get_border_rects(field, SCREEN_RECT)
        if field.collidepoint(reimu.rect.centerx, reimu.rect.centery):
            color = (255,0,0)
            self.x += self.vel_x
            self.y += self.vel_y
        else:
            color = (255, 255, 255)
            if self.vel_x > 0 and self.vel_y > 0:
                self.x -= 10
                self.y -= 10
                self.x -= self.vel_x*2
                self.y -= self.vel_y*2
            elif self.vel_x < 0 and self.vel_y < 0:
                self.x += 10
                self.y += 10
                self.x += self.vel_x*2
                self.y += self.vel_y*2
            elif self.vel_x > 0 and self.vel_y < 0:
                self.x -= 10
                self.y += 10
                self.x -= self.vel_x*2
                self.y += self.vel_y*2
            elif self.vel_x < 0 and self.vel_y > 0:
                self.x += 10
                self.y -= 10
                self.x += self.vel_x*2
                self.y -= self.vel_y*2
            # VARIABLES
            elif self.vel_x > 0 and self.vel_y == 0:
                self.x -= 10
                self.x -= self.vel_x*2
            elif self.vel_x < 0 and self.vel_y == 0:
                self.x += 10
                self.x += self.vel_x*2
            elif self.vel_x == 0 and self.vel_y < 0:
                self.y += 10
                self.y += self.vel_y*2
            elif self.vel_x == 0 and self.vel_y > 0:
                self.y -= 10
                self.y -= self.vel_y*2

        for border_rect in border_rects:
            pygame.draw.rect(SCREEN, color, border_rect)

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

class Nazrin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #----------------------
        # Basic init stuff
        pygame.sprite.Sprite.__init__(self)
        self.image = nazrin_sp_1_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.x = int(start_localizations['nazrin'][0])
        self.y = int(start_localizations['nazrin'][1])
        

        #----------------------
        #Movement system utilities
        self.velX = 0
        self.velY = 0
        self.speed = 4

        #----------------------
        #Collision system utilities
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def move(self, direction):
        #----------------------
        #Movement system utilities
        self.vel_x = 0
        self.vel_y = 0
        global nazrin_velocity
        nazrin_velocity = (self.vel_x, self.vel_y)
        speed_diviser_value = 2
        if direction == "left" and not direction == "right":
            self.vel_x = -self.speed / speed_diviser_value
        if direction == "right" and not direction == "left":
            self.vel_x = self.speed / speed_diviser_value
        if direction == "up" and not direction == "down":
            self.vel_y = -self.speed / speed_diviser_value
        if direction == "down" and not direction == "up":
            self.vel_y = self.speed / speed_diviser_value
    
    def update(self):
        self.rect = pygame.Rect(int(self.x), int(self.y), int(self.x), int(self.y))


reimu = Reimu(start_localizations["reimu"][0], start_localizations["reimu"][1])
reimu.rect.center = SCREEN_RECT.center
all_sprites.add(reimu)

nazrin = Nazrin(start_localizations["nazrin"][0], start_localizations["nazrin"][1])
nazrin.rect.center = SCREEN_RECT.center
all_sprites.add(nazrin)


# Dialogue System -----------------------------------------------
def draw_speech_bubble(screen, text, text_colour, bg_colour, pos, size):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, text_colour)
    text_rect = text_surface.get_rect(midbottom=pos)

    # background
    bg_rect = text_rect.copy()
    bg_rect.inflate_ip(10, 10)

    # Frame
    frame_rect = bg_rect.copy()
    frame_rect.inflate_ip(4, 4)

    pygame.draw.rect(screen, text_colour, frame_rect)
    pygame.draw.rect(screen, bg_colour, bg_rect)
    screen.blit(text_surface, text_rect)


# dialogue item format: (screen, text, text_colour, bg_colour, pos, size)
def dialogueSystem(dialogueList):
    speaking = True
    for dialogueItem in dialogueList:
        SCREEN.blit(dialogueItem[0], (0,0))
        if speaking:
            draw_speech_bubble(dialogueItem[1], dialogueItem[2], dialogueItem[3], dialogueItem[4], dialogueItem[5], dialogueItem[6])
def play():
    while True:
        # Texts ----------------------------------------------------------- # We are packing the TEXT_TEXT and the TEXT_RECT in tuples so we can pass them in a "for each" to blit them on screen 
        TITLE_TEXT = get_font_yuki_boku(45).render("東方Project", True, "White")
        TITLE_RECT = TITLE_TEXT.get_rect(center=(950, 50))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        TEXTS_CONTAINER = [[TITLE_TEXT, TITLE_RECT]]


        # Event handler ----------------------------------------------------------- #
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        dialogueItem = [SCREEN, "Hello there.", (255, 255, 255), (40, 40, 40), reimu.rect.midtop, 25]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    # dialogue item format: (screen, text, text_colour, bg_colour, pos, size)
                    dialogueSystem([[nazrin_sp_1_img, SCREEN, "Hello there.", (255, 255, 255), (40, 40, 40), reimu.rect.midtop, 25]])
                if event.key == pygame.K_9:
                    font = pygame.font.SysFont(None, dialogueItem[5])
                    text_surface = font.render(dialogueItem[1], True, dialogueItem[2])
                    text_rect = text_surface.get_rect(midbottom=dialogueItem[4])

                    # background
                    bg_rect = text_rect.copy()
                    bg_rect.inflate_ip(10, 10)

                    # Frame
                    frame_rect = bg_rect.copy()
                    frame_rect.inflate_ip(4, 4)

                    pygame.draw.rect(dialogueItem[0], dialogueItem[2], frame_rect)
                    pygame.draw.rect(dialogueItem[0], dialogueItem[3], bg_rect)
                    SCREEN.blit(text_surface, text_rect)
                if event.key == pygame.K_LEFT:
                    reimu.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    reimu.right_pressed = True
                if event.key == pygame.K_UP:
                    reimu.up_pressed = True
                if event.key == pygame.K_DOWN:
                    reimu.down_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    reimu.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    reimu.right_pressed = False
                if event.key == pygame.K_UP:
                    reimu.up_pressed = False
                if event.key == pygame.K_DOWN:
                    reimu.down_pressed = False


        # Display handler ----------------------------------------------------------- #
        '''
        SCREEN.blit(awoo_img, (0, 0))
        all_sprites.update()
        all_sprites.draw(SCREEN)
        for text in TEXTS_CONTAINER:
            SCREEN.blit(text[0], text[1])
        pygame.time.delay(100)
        '''
        pygame.display.update()


    


def options():
    while True:
        # Texts ----------------------------------------------------------- # We are packing the TEXT_TEXT and the TEXT_RECT in tuples so we can pass them in a "for each" to blit them on screen 
        OPTIONS_TEXT = get_font_watatsuki(70).render("Options", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(150, 100))
        OPTIONS_TEXT_CONTAINER = (OPTIONS_TEXT, OPTIONS_RECT)

        VOLUME_TEXT = get_font_watatsuki(40).render("Volume", True, "White")
        VOLUME_RECT = VOLUME_TEXT.get_rect(center=(150, 250))
        VOLUME_TEXT_CONTAINER = (VOLUME_TEXT, VOLUME_RECT)

        TEXTS_CONTAINER = [OPTIONS_TEXT_CONTAINER, VOLUME_TEXT_CONTAINER]


        # Buttons ----------------------------------------------------------- #
        VOLUME_DOWN = Button(image=button_rect_2, pos=(200, 300), 
                            text_input="DOWN", font=get_font_watatsuki(22), base_color="#d7fcd4", hovering_color="Yellow")
        VOLUME_UP = Button(image=button_rect_2, pos=(600, 300),
                            text_input="UP", font=get_font_watatsuki(22), base_color="#d7fcd4", hovering_color="Yellow")
        MAIN_MENU_BUTTON = Button(image=button_rect_2, pos=(150, 800), 
                            text_input="Return to main menu", font=get_font_watatsuki(22), base_color="#d7fcd4", hovering_color="Yellow")
                            
        
        # Event handler ----------------------------------------------------------- #
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOLUME_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                    play()
                if VOLUME_UP.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MAIN_MENU_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    mainMenu()


        # Display handler ----------------------------------------------------------- #
        SCREEN.blit(menu_bg_img, (0, 0))

        for text in TEXTS_CONTAINER:
            SCREEN.blit(text[0], text[1])

        for button in [VOLUME_DOWN, VOLUME_UP, MAIN_MENU_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        pygame.display.update()



def mainMenu():
    if ost_channel.get_busy == False:
        ost_channel.play(menu_theme)
        
    while True:
        # Audio pygame mixer --------------------------------------------------------------
        SCREEN.blit(menu_bg_img, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font_yuki_boku(120).render("東方Project", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=button_rect_1, pos=(300, 300), 
                            text_input="Start", font=get_font_watatsuki(30), base_color="#d7fcd4", hovering_color="Yellow")
        OPTIONS_BUTTON = Button(image=button_rect_1, pos=(300, 400), 
                            text_input="Options", font=get_font_watatsuki(30), base_color="#d7fcd4", hovering_color="Yellow")
        QUIT_BUTTON = Button(image=button_rect_1, pos=(300, 500),
                            text_input="Exit", font=get_font_watatsuki(30), base_color="#d7fcd4", hovering_color="Yellow")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

mainMenu()