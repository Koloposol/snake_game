import pygame as pg
from random import randrange

pg.display.set_caption("Snake")

#Константы
RES = 800
SIZE = 40
FPS = 10

def get_random_position():
    return randrange(0, RES, SIZE), randrange(0, RES, SIZE)

#Начальное положение змейки и еды
x, y = get_random_position()
food = get_random_position()

#Блокировка клавишь
dirs = {'W': True, 'S': True, 'A': True, 'D': True}

#Параметры змейки
length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
hight_score = 0

#Запуск игры
pg.init()
game_screen = pg.display.set_mode([RES, RES])
clock = pg.time.Clock()

#Параметры шрифта
font_score = pg.font.SysFont("Consolas", 26, bold = True)
font_total_score = pg.font.SysFont("Consolas", 48, bold = True)
font_hight_score = pg.font.SysFont("Consolas", 48, bold = True)
font_end = pg.font.SysFont("Consolas", 68, bold = True)
font_message = pg.font.SysFont("Consolas", 26, bold = True)

#Параметры звука
eat_sound = pg.mixer.Sound("eat.wav")
game_over_sound = pg.mixer.Sound("game_over.wav")

while True:
    game_screen.fill((155, 188, 15))

    #Рисуем змейку и еду
    [(pg.draw.rect(game_screen, (120, 149, 12), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pg.draw.rect(game_screen, (15, 56, 15), (*food, SIZE, SIZE))
    
    #Счетчик очков
    render_score = font_score.render(f"SCORE: {score}", 1, (48, 98, 48))
    game_screen.blit(render_score, (5, 5))

    #Движение змейки
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    #Поедание
    if snake[-1] == food:
        food = get_random_position()
        length += 1
        score += 1
        eat_sound.play()

    #Проигрышь
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        
        game_over_sound.play()
        
        if score > hight_score:
            hight_score = score

        while True:
            render_end = font_end.render("GAME OVER", 1, (48, 98, 48))
            render_hight_score = font_hight_score.render(f"HIGHT SCORE: {hight_score}", 1, (48, 98, 48))
            render_total_score = font_total_score.render(f"SCORE: {score}", 1, (48, 98, 48))
            render_message = font_message.render("Press Q for exit or R for restart", 1, (48, 98, 48))
            game_screen.blit(render_end, (RES // 2 - 160, RES // 3))
            game_screen.blit(render_hight_score, (RES // 2 - 170, RES // 2.3))
            game_screen.blit(render_total_score, (RES // 2 - 100, RES // 2))
            game_screen.blit(render_message, (RES // 2 - 220, RES // 1.7))
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            #Меню выбора Выход/Рестарт
            key = pg.key.get_pressed()
            if key[pg.K_q]:
                exit()
            elif key[pg.K_r]:
                score = 0
                x, y = get_random_position()
                food = get_random_position()
                length = 1
                break
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