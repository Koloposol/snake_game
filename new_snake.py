import pygame as pg
from random import randrange

RES = 800
SIZE = 40
def get_random_position():
    return randrange(0, RES, SIZE), randrange(0, RES, SIZE)

#Начальное положение змейки и еды
x, y = get_random_position()
food = get_random_position()

#Кнопки
dirs = {'W': True, 'S': True, 'A': True, 'D': True}

#Параметры змейки
length = 1
snake = [(x, y)]
dx, dy = 0, 0
FPS = 10

pg.init()
game_screen = pg.display.set_mode([RES, RES])
clock = pg.time.Clock()

while True:
    game_screen.fill((155, 188, 15))

    #Рисуем змейку и еду
    [(pg.draw.rect(game_screen, (120, 149, 12), (i, j, SIZE, SIZE))) for i, j in snake]
    pg.draw.rect(game_screen, (15, 56, 15), (*food, SIZE, SIZE))

    #Движение змейки
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    #Поедание
    if snake[-1] == food:
        food = get_random_position()
        length += 1

    #Проигрышь
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        x, y = get_random_position()
        food = get_random_position()
        length = 1
    # if len(snake) != len(set(snake)):
    #     x, y = get_random_position()
    #     food = get_random_position()
    #     length = 1

    pg.display.flip()
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    #Управление
    key = pg.key.get_pressed()
    if key[pg.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pg.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pg.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pg.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}