import json
import time
import numpy as np
import pygame



it_max = int(input("Max iterations: "))
pygame.init()
size = width, height = 1024, 1024
liveCellColor = (255, 255, 255)
deadCellColor = (25, 25, 25)
screen = pygame.display.set_mode(size)

x_size = 512
y_size = 512
x_bound = x_size - 1
y_bound = y_size - 1

square_off = int(size[0]/(x_size-2))

buff_1 = np.random.choice(a = [False, True, True], size = (x_size, y_size))
buff_2 = np.zeros(shape=(x_size, y_size), dtype=bool)

for y, e in enumerate(buff_1):
    for x, val in enumerate(e):
        if (y == 0 or x == 0 or x == x_bound or y == y_bound):
            buff_1[y, x] = False

buff = []
buff.append(buff_1)
buff.append(buff_2)




for i in range(it_max):
    changed = False
    screen.fill(deadCellColor)
    for y in range(1, y_bound):
        for x in range(1, x_bound):
            buff[1][y, x] = False
            count = 0

            if (buff[0][y - 1, x]):
                count += 1
            if (buff[0][y - 1, x - 1]):
                count += 1
            if (buff[0][y - 1, x + 1]):
                count += 1
            if (buff[0][y, x - 1]):
                count += 1
            if (buff[0][y + 1, x - 1]):
                count += 1
            if (buff[0][y + 1, x + 1]):
                count += 1
            if (buff[0][y + 1, x]):
                count += 1
            if (buff[0][y, x + 1]):
                count += 1

            if (not(buff[0][y, x]) and 
            count == 3):
                buff[1][y, x] = True
                changed = True
                screen.fill(liveCellColor, rect=(square_off*(y-1), square_off*(x-1), square_off, square_off))
            if (buff[0][y, x] and 
            count < 2 or count > 3):
                buff[1][y, x] = False
                changed = True
    pygame.display.flip()
    
    if (buff[0] is buff_1):
        buff[0] = buff_2
        buff[1] = buff_1
    else:
        buff[0] = buff_1
        buff[1] = buff_2


    if not(changed):
        print(f'Last iteration: {i}')
        break
    


