import pygame
import sys
import os
import random
import math


all_sprites = pygame.sprite.Group()
FPS = 50
pygame.display.set_caption('Casino')
check = False
check1 = False
winlose = ''
screen_size = (500, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
f = open('data/score.txt', 'r')
score = int(*f)


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


def casino():
    intro_text = ["                           Сделайте ставку",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  f"               Голда: {score}              ",
                  "                                           ",
                  "                                           ",
                  "                                           ",
                  "              Проверить удачу (стрелка вверх)",
                  "                                           ",
                  "                    Вернуться назад (пробел) ",
                  ]
    screen.fill('black')
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


class B2(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("x2_icon.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 150

    def update(self, *args):
        global check
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos) and not check and not check1:
            self.image = load_image("x2_icona.png")
            check = True
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos) and check:
            self.image = load_image("x2_icon.png")
            check = False

    def backer(self):
        global check
        self.image = load_image("x2_icon.png")
        check = False


class B4(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("x4_icon.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 150

    def update(self, *args):
        global check1
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos) and not check1 and not check:
            self.image = load_image("x4_icona.png")
            check1 = True
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos) and check1:
            self.image = load_image("x4_icon.png")
            check1 = False

    def backer(self):
        global check1
        self.image = load_image("x4_icon.png")
        check1 = False


class WL(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("nothing.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 380

    def update(self):
        global winlose
        if winlose == 'x2_win':
            self.image = load_image("x2_win.png")
        if winlose == 'x4_win':
            self.image = load_image("x4_win.png")
        if winlose == 'x4_lose':
            self.image = load_image("x4_lose.png")
        if winlose == 'x2_lose':
            self.image = load_image("x2_lose.png")
        if winlose == 'nothing':
            self.image = load_image("nothing.png")

    def backer(self):
        global check1
        self.image = load_image("x4_icon.png")
        check1 = False


if __name__ == '__main__':
    pygame.init()
    running = True
    b = B2()
    c = B4()
    WL = WL()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if check:
                        a = 1
                        x = random.randrange(1, 3)
                        if a == x:
                            score = math.ceil(score * 1.2)
                            winlose = 'x2_win'
                            WL.update()
                        else:
                            score = math.ceil(score * 0.8)
                            winlose = 'x2_lose'
                            WL.update()
                    elif check1:
                        a = 1
                        x = random.randrange(1, 5)
                        if a == x:
                            score = math.ceil(score * 1.4)
                            winlose = 'x4_win'
                            WL.update()
                        else:
                            score = math.ceil(score * 0.6)
                            winlose = 'x4_lose'
                            WL.update()
                    open('data/score.txt', 'w').write(str(score))
                    b.backer()
                    c.backer()
                    b.update(event)
                    c.update(event)
                if event.key == pygame.K_SPACE:
                    sys.exit()
            casino()
            b.update(event)
            c.update(event)
            WL.update()
            pygame.time.Clock().tick(30)
            all_sprites.add(b, c, WL)
            all_sprites.draw(screen)
            all_sprites.remove(b)
            all_sprites.remove(c)
            all_sprites.remove(WL)
            b.update()
            c.update()
            WL.update()
            pygame.display.flip()
    pygame.quit()
