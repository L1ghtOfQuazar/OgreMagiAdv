import pygame
import sys
import os
import subprocess


FPS = 50
pygame.init()
screen_size = (500, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.display.set_caption('Main menu')


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    pygame.display.set_caption('Main menu')
    intro_text = ["                   Ogre Magi fun adventures",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                Правила игры (стрелка вверх)",
                  "                                           ",
                  "                      Об игре (стрелка вниз)",
                  "                                           ",
                  "                        Начать игру (пробел)  ",
                  ]

    fon = pygame.transform.scale(load_image('start_screen.jpg'), (500, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    rules()
                if event.key == pygame.K_DOWN:
                    about()
                if event.key == pygame.K_SPACE:
                    start()

        pygame.display.flip()
        clock.tick(FPS)


def rules():
    pygame.display.set_caption('Rules')
    intro_text = ["                              Правила игры   ",
                  "  В игре представлено два игровых режима:    ",
                  "  Multicast casino и The labyrinth of bloodlust.",
                  "  Целью игры является добыча голды.",
                  "  Получить ее можно играя в ",
                  "  The labyrinth of bloodlust, ",
                  "  Или делая ставки в Multicast casino.                                        ",
                  "  Управление:                              ",
                  "  Multicast casino: Выберите коэффицент     ",
                  "  И нажмите стрелку вверх для прокрутки.    ",
                  "  Выбор коэффицента можно отменить",
                  "  Повторным нажатием.                      ",
                  "  Ставка равна 10% от всей голды.          ",
                  "  The labyrinth of bloodlust:              ",
                  "  Передвигая персонажа стрелками           ",
                  "  Собирайте Tome of Knolege                ",
                  "  И получайте за это голду.                ",
                  "                   Вернуться назад (пробел)  ",
                  ]
    fon = pygame.transform.scale(load_image('start_screen.jpg'), (500, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    start_screen()
        pygame.display.flip()
        clock.tick(FPS)


def about():
    pygame.display.set_caption('About game')
    intro_text = ["                                  Об игре   ",
                  "Добро пожаловать в веселые приключения ",
                  "Огре Маги! Огре Маги - счастливый огр, ",
                  "Отличающейся высокой удачей и умом, что не ",
                  "Характерно для его сородичей.",
                  "Помогите огру стать умнее,",
                  "Собирая книги знаний в лабиринте,",
                  "А также удачливее, играя в казино!",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "Все изображения взяты из открытых источников",
                  "И используются в некоммерческих целях.",
                  "                                           ",
                  "                                           ",
                  "                   Вернуться назад (пробел)  ",
                  ]
    fon = pygame.transform.scale(load_image('start_screen.jpg'), (500, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    start_screen()
        pygame.display.flip()
        clock.tick(FPS)


def start():
    pygame.display.set_caption('Start')
    intro_text = ["                           Выберите режим",
                  "                                           ",
                  "             Multicast                      The labyrinth",
                  "             casino                           of bloodlust",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                 Первая игра (стрелка влево)",
                  "                                           ",
                  "                Вторая игра (стрелка вправо)",
                  "                                           ",
                  "                  Вернуться назад (пробел) ",
                  ]
    cas = pygame.transform.scale(load_image('multicast_icon.png'), (100, 100))
    cas_rect = cas.get_rect(center=(130, 230))
    laby = pygame.transform.scale(load_image('bloodlust_icon.png'), (100, 100))
    laby_rect = laby.get_rect(center=(370, 230))
    fon = pygame.transform.scale(load_image('start.jpg'), (500, 600))
    screen.blit(fon, (0, 0))
    screen.blit(cas, cas_rect)
    screen.blit(laby, laby_rect)
    font = pygame.font.Font(None, 30)
    pygame.display.update()
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ca()
                if event.key == pygame.K_RIGHT:
                    la()
                if event.key == pygame.K_SPACE:
                    start_screen()
        pygame.display.flip()
        clock.tick(FPS)


def ca():
    global screen
    pygame.display.set_mode(screen_size, flags=pygame.HIDDEN)
    subprocess.call("casino.py", shell=True)
    pygame.display.set_mode(screen_size, flags=pygame.SHOWN)
    start()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


def la():
    global screen
    pygame.display.set_mode(screen_size, flags=pygame.HIDDEN)
    subprocess.call("laby.py", shell=True)
    pygame.display.set_mode(screen_size, flags=pygame.SHOWN)
    start()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


start_screen()
