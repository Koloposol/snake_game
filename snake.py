import pygame as pg
from random import randrange

#Константы
WINDOW = 800
FPS = 60
TILE_SIZE = 40
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

#Функция для определения координат (X:Y) случайной позиции на игровом поле
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]

#Параметры змейки
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)

#Параметры объектов еды
food = snake.copy()
food.center = get_random_position()

#Параметры времени и задержки
time = 0
time_step = 110

#Инициализация объектов
game_screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

#Главный цикл игры
while True:
    #Частота обновления экрана
    clock.tick(FPS)

    #Цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        
        game_screen.fill((155, 188, 15))

        #Рисуем объект еды
        pg.draw.rect(game_screen, (15, 56, 15), food)

        #Рисуем змейку
        [pg.draw.rect(game_screen, (120, 149, 12), segment) for segment in segments]

        #Обработка нажатий WASD
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)

        #Управление змейкой
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]

        #Поедание
        if snake.center == food.center:
            food.center = get_random_position()
            length += 1

        #Столкновение с границами и телом змейки
        snake_collision = pg.Rect.collidelist(snake, segments[:-1]) != -1
        if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or snake_collision:
            snake.center, food.center = get_random_position(), get_random_position()
            length, snake_dir = 1, (0, 0)
            segments = [snake.copy()]

        pg.display.flip()