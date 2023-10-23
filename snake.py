import pygame as pg
from random import randrange

#Константы
WINDOW = 800
FPS = 60

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
        pg.display.flip()