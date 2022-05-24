"""
Игра жизнь v.0.1
Мое изучение и эксперименты
"""
import sys
import numpy as np
import pygame
from pygame.color import THECOLORS

side_square = 5  # Сторона квадрата
num_square = 200  # Количество квадратов
X_working_field = side_square * num_square  # Ширина рабочего поля в пикселах
Y_working_field = side_square * num_square  # Высота рабочего поля в пикселах

X_square = int(X_working_field / side_square)  # Количество квадратиков по оси X
Y_square = int(Y_working_field / side_square)  # Количество квадратиков по оси Y

Life_working_array = np.random.randint(0, 20, (X_square, Y_square))  # Заполняем массив значениями от "0" до "1"
# Life_working_array = np.zeros((X_square, Y_square))
# Life_working_array[3][2] = 1
# Life_working_array[3][3] = 1
# Life_working_array[3][4] = 1
Life_temp_array = np.zeros((X_square, Y_square))  # Заполняем массив значениями "0"
print(Life_working_array)

pygame.init()
screen = pygame.display.set_mode((X_working_field, Y_working_field))


def drawing():
    screen.fill(THECOLORS['black'])
    for i in range(X_square):
        for j in range(Y_square):
            r = pygame.Rect((0 + i * side_square, 0 + j * side_square), (side_square, side_square))
            if Life_working_array[i][j] == 1:
                r_width = 1
            else:
                r_width = 0
                Life_working_array[i][j] = 0
            pygame.draw.rect(screen, (255, 255, 255), r, width=r_width)


def new_position():
    for i in range(X_square):
        for j in range(Y_square):
            living_cell = 0  # Количество живых клеток вокруг
            for k in range(8):
                if k + 1 == 1:
                    ii = i
                    jj = j - 1 if j - 1 >= 0 else Y_square - 1
                    if Life_working_array[ii][jj] == 1:
                        living_cell += 1
                elif k + 1 == 2:
                    ii = i + 1 if i + 1 != X_square else 0
                    jj = j - 1 if j - 1 >= 0 else Y_square - 1
                    if Life_working_array[ii][jj] == 1:
                        living_cell += 1
                elif k + 1 == 3:
                    ii = i + 1 if i + 1 != X_square else 0
                    jj = j
                    if Life_working_array[ii][jj] == 1:
                        living_cell += 1
                elif k + 1 == 4:
                    ii = i + 1 if i + 1 != X_square else 0
                    jj = j + 1 if j + 1 != Y_square else 0
                    if Life_working_array[ii][jj] == 1:
                        living_cell += 1
                elif k + 1 == 5:
                    ii = i
                    jj = j + 1 if j + 1 != Y_square else 0
                    if Life_working_array[ii][jj] == 1:
                        living_cell += 1
                elif k + 1 == 6:
                    ii = i - 1 if i - 1 >= 0 else X_square - 1
                    jj = j + 1 if j + 1 != Y_square else 0
                    if Life_working_array[ii][jj] == 1:
                        living_cell += 1
                elif k + 1 == 7:
                    ii = i - 1 if i - 1 >= 0 else X_square - 1
                    jj = j
                    if Life_working_array[ii][jj] == 1:
                        living_cell += 1
                elif k + 1 == 8:
                    ii = i - 1 if i - 1 >= 0 else X_square - 1
                    jj = j - 1 if j - 1 >= 0 else Y_square - 1
                    if Life_working_array[ii][jj] == 1:
                        living_cell += 1
            if Life_working_array[i][j] == 0:  # Мертвая клетка
                if living_cell == 3:
                    Life_temp_array[i][j] = 1
                else:
                    Life_temp_array[i][j] = 0
            else:  # Живая клетка
                if living_cell == 2 or living_cell == 3:
                    Life_temp_array[i][j] = 1
                else:
                    Life_temp_array[i][j] = 0
    for i in range(X_square):
        for j in range(Y_square):
            Life_working_array[i][j] = Life_temp_array[i][j]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    drawing()
    pygame.display.update()
    new_position()
    # sleep(0.2)
    # print("---------------------------")
