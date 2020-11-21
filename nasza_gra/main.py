<<<<<<< HEAD
import pygame
import pygame.sysfont
from pygame.locals import *
import os

#pygame.sysfont.initsysfonts()
pygame.init()
#pygame.mixer.init()
FPS= 60

# szerokość i wysokość okna gry
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# robienie sciezek wzglednych
grafiki = os.path.dirname(__file__)
player_test_png = os.path.join(grafiki, 'grafiki\player_test.png')
map_dont_ask_png = os.path.join(grafiki, 'grafiki\map_dont_ask.png')
m_font= os.path.join(grafiki, 'grafiki\PixelEmulator-xq08.ttf')
BACKGROUND_COLOR = pygame.image.load(os.path.join(grafiki, 'grafiki\\bground.png'))

# OKNO GRY
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nasza gra') # nazwa okna
CLOCK = pygame.time.Clock()
#icon = pygame.image.load('nazwa')  # zmiana ikonki
#pygame.display.set_icon(icon)

# KOLORY
#BACKGROUND_COLOR = (204, 255, 153)
BLACK = (0, 0, 0)
BRIGHT_BLACK = (138, 138, 138)
WHITE = (255, 255, 255)

# FUNCKJE

def text_objects(text, font, color):
    textSurface= font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text): #wyświetlanie wiadomości w grze
    largeText= pygame.font.SysFont(text, 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2))
    SCREEN.blit(TextSurf,TextRect)
    pygame.display.update()


def whether_exit(event):     # tu nie ma petli for, tylko warunki
    if event.type == QUIT:
        pygame.quit()
        quit()
    elif event.type == pygame.KEYDOWN:
         if event.key == K_ESCAPE:   # wyjście escapem
            pygame.quit()
            quit()

def button(msg, x, y, width, height, icolor, acolor, action=None):
    MOUSE = pygame.mouse.get_pos()
    CLICK= pygame.mouse.get_pressed()
    if x + width > MOUSE[0] > x and y + height > MOUSE[1] > y:
        pygame.draw.rect(SCREEN, acolor, (x, y, width, height))
        if CLICK[0]== 1 and action != None:
            if action == 'play':
                game_loop()
            elif action == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(SCREEN, icolor, (x, y, width, height))
    smallText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(msg, smallText, WHITE)
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    SCREEN.blit(TextSurf, TextRect)
    pygame.display.update()


def m_menu():
    M_MENU= True
    while M_MENU:
        for event in pygame.event.get():
            whether_exit(event)
        SCREEN.blit(BACKGROUND_COLOR, [0,0] )  # kolor okna gry
        largeText = pygame.font.Font(m_font, 115)
        TextSurf, TextRect = text_objects("Nasza Gra", largeText, BLACK)  #zmienić nazwę jak już wymyślimy
        TextRect.center = ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT-600))
        SCREEN.blit(TextSurf, TextRect)
        #pygame.mixer.music.load(os.path.join('intro.wav'))  # intro
        #pygame.mixer.music.set_volume(0.20)
        #pygame.mixer.music.play(-1)

        # rysowanie obiektów
        MOUSE = pygame.mouse.get_pos()

        button('Zagraj', 200, 600, 300, 120, BLACK, BRIGHT_BLACK, 'play')
        button('Wyjdź', 700, 600, 300, 120, BLACK, BRIGHT_BLACK, 'quit')


        pygame.display.update()
        CLOCK.tick(FPS)

# gracz
gracz_ikona = pygame.image.load(player_test_png)
playerX = WINDOW_WIDTH/2
playerY = WINDOW_HEIGHT/2
def gracz_wyswietl():
    global playerX, playerY
    SCREEN.blit(gracz_ikona, (playerX, playerY))

# mapa
mapa = pygame.image.load(map_dont_ask_png)
mapaX = 100
mapaY = 100
mapaX_step = 0
mapaY_step = 0

def mapa_wyswietl():
    global mapaX, mapaY
    SCREEN.blit(mapa, (mapaX, mapaY))


# poruszanie "sie"
def ruch_mapy():
    global mapaX, mapaY, mapaX_step, mapaY_step
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mapaY_step = 10
            elif event.key == pygame.K_DOWN:
                mapaY_step = -10
            elif event.key == pygame.K_LEFT:
                mapaX_step = 10
            elif event.key == pygame.K_RIGHT:
                mapaX_step = -10

        #mapaX += mapaX_step
        #mapaY += mapaY_step

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mapaX_step = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                mapaY_step = 0

        whether_exit(event)

# PĘTLA GŁówna PROGRAMU
def game_loop():
    while True:
        global mapaX, mapaY, mapaX_step, mapaY_step
        CLOCK.tick(FPS)
        SCREEN.fill(WHITE)

        mapa_wyswietl()
        gracz_wyswietl()
        ruch_mapy()
        mapaX += mapaX_step
        mapaY += mapaY_step
        pygame.display.update()     #aktualizuje wszystkie parametry ekranu na bieżąco

m_menu()
# KONIEC
=======
import pygame
import pygame.sysfont
from pygame import mixer
from pygame.locals import *
import os

#pygame.sysfont.initsysfonts()
pygame.init()
pygame.mixer.init()
FPS = 60

# szerokość i wysokość okna gry
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# robienie sciezek wzglednych
grafiki = os.path.dirname(__file__)
player_test_png = os.path.join(grafiki, 'grafiki\player_test.png')
map_dont_ask_png = os.path.join(grafiki, 'grafiki\map_dont_ask.png')
m_font = os.path.join(grafiki, 'grafiki\PixelEmulator-xq08.ttf')
BACKGROUND_COLOR = pygame.image.load(os.path.join(grafiki, 'grafiki\\bground.png'))


# OKNO GRY
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nasza gra')  # nazwa okna
CLOCK = pygame.time.Clock()
#icon = pygame.image.load('nazwa')  # zmiana ikonki
#pygame.display.set_icon(icon)

# KOLORY
#BACKGROUND_COLOR = (204, 255, 153)
BLACK = (0, 0, 0)
BRIGHT_BLACK = (138, 138, 138)
WHITE = (255, 255, 255)

#  ODGŁOSY CHODZENIA


# FUNCKJE

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):  # wyświetlanie wiadomości w grze
    largeText = pygame.font.SysFont(text, 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2))
    SCREEN.blit(TextSurf, TextRect)
    pygame.display.update()


def whether_exit(event):     # tu nie ma petli for, tylko warunki
    if event.type == QUIT:
        pygame.quit()
        quit()
    elif event.type == pygame.KEYDOWN:
        if event.key == K_ESCAPE:   # wyjście escapem
            pygame.quit()
            quit()


def button(msg, x, y, width, height, icolor, acolor, action=None):  # wymiary okna gry zostały zmienione zmienić lokalizaję przycisków
    MOUSE = pygame.mouse.get_pos()
    CLICK = pygame.mouse.get_pressed()
    if x + width > MOUSE[0] > x and y + height > MOUSE[1] > y:
        pygame.draw.rect(SCREEN, acolor, (x, y, width, height))
        if CLICK[0] == 1 and action != None:
            if action == 'play':
                game_loop()
            elif action == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(SCREEN, icolor, (x, y, width, height))
    smallText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(msg, smallText, WHITE)
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    SCREEN.blit(TextSurf, TextRect)
    pygame.display.update()


def m_menu():
    mixer.music.load("intro.mp3")
    pygame.mixer.music.set_volume(0.4)
    mixer.music.play(-1)
    pygame.event.wait()

    M_MENU = True
    while M_MENU:
        for event in pygame.event.get():
            whether_exit(event)
        SCREEN.blit(BACKGROUND_COLOR, [0, 0])  # kolor okna gry
        largeText = pygame.font.Font(m_font, 115)
        TextSurf, TextRect = text_objects("Nasza Gra", largeText, BLACK)  # zmienić nazwę jak już wymyślimy
        TextRect.center = ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT-600))
        SCREEN.blit(TextSurf, TextRect)

        # rysowanie obiektów
        MOUSE = pygame.mouse.get_pos()

        button('Zagraj', 200, 600, 300, 120, BLACK, BRIGHT_BLACK, 'play')
        button('Wyjdź', 700, 600, 300, 120, BLACK, BRIGHT_BLACK, 'quit')

        pygame.display.update()
        CLOCK.tick(FPS)


# gracz
gracz_ikona = pygame.image.load(player_test_png)
playerX = WINDOW_WIDTH/2
playerY = WINDOW_HEIGHT/2


def gracz_wyswietl():
    global playerX, playerY
    SCREEN.blit(gracz_ikona, (playerX, playerY))


# mapa
mapa = pygame.image.load(map_dont_ask_png)
mapaX = 100
mapaY = 100
mapaX_step = 0
mapaY_step = 0


def mapa_wyswietl():
    global mapaX, mapaY
    SCREEN.blit(mapa, (mapaX, mapaY))


# poruszanie "sie"
def ruch_mapy():
    global mapaX, mapaY, mapaX_step, mapaY_step
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mapaY_step = 10
            elif event.key == pygame.K_DOWN:
                mapaY_step = -10
            elif event.key == pygame.K_LEFT:
                mapaX_step = 10
            elif event.key == pygame.K_RIGHT:
                mapaX_step = -10



        #mapaX += mapaX_step
        #mapaY += mapaY_step

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mapaX_step = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                mapaY_step = 0

        whether_exit(event)


# PĘTLA GŁówna PROGRAMU
def game_loop():
    pygame.mixer.music.stop()
    mixer.music.load("background.mp3")  # gra muzykę w tle
    pygame.mixer.music.set_volume(0.3)
    mixer.music.play(-1)
    pygame.event.wait()

    while True:
        global mapaX, mapaY, mapaX_step, mapaY_step
        CLOCK.tick(FPS)
        SCREEN.fill(WHITE)

        mapa_wyswietl()
        gracz_wyswietl()
        ruch_mapy()
        mapaX += mapaX_step
        mapaY += mapaY_step
        pygame.display.update()  # aktualizuje wszystkie parametry ekranu na bieżąco


m_menu()
# KONIEC
>>>>>>> 808790df60d20fe2646c505bbf80e61cf32b7b0c
