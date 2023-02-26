import pygame
import os
import sys
import random


sg = 0
f = open('data/score.txt', 'r')
score = int(*f)
pygame.display.set_caption('The labyrinth of bloodlust')
pygame.init()
screen_size = (1000, 600)
screen = pygame.display.set_mode(screen_size)
FPS = 50


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


tile_images = {
    'wall': load_image('tree.png'),
    'empty': load_image('sand.png'),
    'tome': load_image('tome.png'),
}
player_image = load_image('nothing.png')

tile_width = tile_height = 50


def outp():
    intro_text = ["                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",

                  f"Голда: {score}",
                  f"Передвижение (Стрелочки)                                                                                          Остаток книг: {sg}",
                  f"Вернуться назад (пробел)                                                                                    Осталось времени: {counter}"
                  ]

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


class ScreenFrame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = (0, 0, 500, 500)


class SpriteGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def get_event(self, event):
        for sprite in self:
            sprite.get_event(event)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass


class Tile(Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Tomee(Sprite):
    def __init__(self, a, pos_x, pos_y):
        super().__init__(sprite_group)
        if a:
            self.image = tile_images['tome']
        else:
            self.image = tile_images['empty']
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hero_group)
        self.image = load_image('pla.png')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 1, tile_height * pos_y + 1)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            tile_width * self.pos[0] + 1, tile_height * self.pos[1] + 1)


player = None
running = True
clock = pygame.time.Clock()
sprite_group = SpriteGroup()
hero_group = SpriteGroup()


def terminate():
    pygame.quit()
    sys.exit


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


def generate_level(level):
    global sg
    sg = 0
    new_player, x, y = None, None, None
    for y in range(len(level)):
        sh = 0
        for x in range(len(level[y])):
            if level[y][x] == '.':
                if random.randint(1, 2) == 1:
                    level[y][x] = 't'
                    Tile('empty', x, y)
                    Tomee(True, x, y)
                    sg = sg + 1
                else:
                    Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
                level[y][x] = "."
    return new_player, x, y


def move(hero, movement):
    global score
    global sg
    x, y = hero.pos
    if movement == "up":
        if y > 0 and level_map[y - 1][x] == "." or level_map[y - 1][x] == "t":
            if level_map[y - 1][x] == "t":
                hero.move(x, y - 1)
                Tomee(False, x, y - 1)
                level_map[y - 1][x] = "."
                score = score + 10
                sg = sg - 1
                open('data/score.txt', 'w').write(str(score))
            else:
                hero.move(x, y - 1)

    elif movement == "down":
        if y < max_y - 1 and level_map[y + 1][x] == "." or level_map[y + 1][x] == "t":
            if level_map[y + 1][x] == "t":
                hero.move(x, y + 1)
                Tomee(False, x, y + 1)
                level_map[y + 1][x] = "."
                score = score + 10
                sg = sg - 1
                open('data/score.txt', 'w').write(str(score))
            else:
                hero.move(x, y + 1)

    elif movement == "left":
        if x > 0 and level_map[y][x - 1] == "." or level_map[y][x - 1] == "t":
            if level_map[y][x - 1] == "t":
                hero.move(x - 1, y)
                Tomee(False, x - 1, y)
                level_map[y][x - 1] = "."
                score = score + 10
                sg = sg - 1
                open('data/score.txt', 'w').write(str(score))
            else:
                hero.move(x - 1, y)
    elif movement == "right":
        if x < max_x - 1 and level_map[y][x + 1] == "." or level_map[y][x + 1] == "t":
            if level_map[y][x + 1] == "t":
                hero.move(x + 1, y)
                Tomee(False, x + 1, y)
                level_map[y][x + 1] = "."
                score = score + 10
                sg = sg - 1
                open('data/score.txt', 'w').write(str(score))
            else:
                hero.move(x + 1, y)


rr = 0
level_map = load_level("map.map")
hero, max_x, max_y = generate_level(level_map)
pygame.time.set_timer(pygame.USEREVENT, 1500, loops=15)
counter = 15

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            counter -= 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move(hero, "up")
            elif event.key == pygame.K_DOWN:
                move(hero, "down")
            elif event.key == pygame.K_LEFT:
                move(hero, "left")
            elif event.key == pygame.K_RIGHT:
                move(hero, "right")
            if counter == 0:
                sg = 0
                counter = 15
                pygame.time.set_timer(pygame.USEREVENT, 1500, loops=15)
            if sg == 0:
                counter = 15
                pygame.time.set_timer(pygame.USEREVENT, 1500, loops=15)
                if rr == 0:
                    rr = 1
                    sprite_group = SpriteGroup()
                    hero_group = SpriteGroup()
                    level_map = load_level("map2.map")
                    hero, max_x, max_y = generate_level(level_map)
                else:
                    rr = 0
                    sprite_group = SpriteGroup()
                    hero_group = SpriteGroup()
                    level_map = load_level("map.map")
                    hero, max_x, max_y = generate_level(level_map)

            if event.key == pygame.K_SPACE:
                sys.exit()
    screen.fill('black')
    outp()
    sprite_group.draw(screen)
    hero_group.draw(screen)
    clock.tick(50)
    pygame.display.flip()
pygame.quit()
