import json
import time
import numpy as np
import pygame

pygame.init()

class conways:
    def __init__(self, size = 100, max_it = 100):
        self.max_it = max_it
        screen_size = width, height = 1024, 1024
        self.liveCellColor = (255, 255, 255)
        self.deadCellColor = (25, 25, 25)
        self.screen = pygame.display.set_mode(screen_size)

        self.x_size = size+2
        self.y_size = size+2
        self.x_bound = self.x_size - 1
        self.y_bound = self.y_size - 1


        self.square_off = int(screen_size[0]/(self.x_size-2))

        self.buff_1 = np.random.choice(a = [False, True, True], size = (self.x_size, self.y_size))
        self.buff_2 = np.zeros(shape=(self.x_size, self.y_size), dtype=bool)

        

        self.buff = []
        self.buff.append(self.buff_1)
        self.buff.append(self.buff_2)


        self.reset(self.buff_1)

    def reset(self, a):
        self.moves = 0
        self.buff_1 = a
        self.buff[0] = self.buff_1
        self.buff[1] = self.buff_2
        for y, e in enumerate(self.buff_1):
            for x, val in enumerate(e):
                if (y == 0 or x == 0 or x == self.x_bound or y == self.y_bound):
                    self.buff_1[y, x] = False
        for y in range(1, self.y_bound):
            for x in range(1, self.x_bound):
                if a[y, x]:
                    self.moves += 1


    def run(self):
        self.screen.fill(self.deadCellColor)
        for i in range(self.max_it):
            changed = False

            for y in range(1, self.y_bound):
                for x in range(1, self.x_bound):
                    self.buff[1][y, x] = False
                    count = 0

                    if (self.buff[0][y - 1, x]):
                        count += 1
                    if (self.buff[0][y - 1, x - 1]):
                        count += 1
                    if (self.buff[0][y - 1, x + 1]):
                        count += 1
                    if (self.buff[0][y, x - 1]):
                        count += 1
                    if (self.buff[0][y + 1, x - 1]):
                        count += 1
                    if (self.buff[0][y + 1, x + 1]):
                        count += 1
                    if (self.buff[0][y + 1, x]):
                        count += 1
                    if (self.buff[0][y, x + 1]):
                        count += 1

                    if (not(self.buff[0][y, x]) and 
                    count == 3):
                        self.buff[1][y, x] = True
                        changed = True
                        self.screen.fill(self.liveCellColor, 
                        rect=(self.square_off*(y-1), self.square_off*(x-1), self.square_off, self.square_off))
                    if (self.buff[0][y, x] and 
                    count < 2 or count > 3):
                        self.buff[1][y, x] = False
                        changed = True
                        self.screen.fill(self.deadCellColor, 
                        rect=(self.square_off*(y-1), self.square_off*(x-1), self.square_off, self.square_off))

            pygame.display.flip()
            if (self.buff[0] is self.buff_1):
                self.buff[0] = self.buff_2
                self.buff[1] = self.buff_1
            else:
                self.buff[0] = self.buff_1
                self.buff[1] = self.buff_2


            if not(changed):
                alive = False
                #print(buff[0])
                for y in range(1, self.y_bound):
                    for x in range(1, self.x_bound):
                        if self.buff[0][y, x]:
                            print(x)
                            alive = True
                            break
                    if alive:
                        break
                if alive:
                    return float('inf')
                else:
                    return i**2 - self.moves
        return self.max_it**2 - self.moves




test = conways()
print(test.run())

test.reset(np.random.choice(a = [False, False,False,False,False,False,False,True], size = (102, 102)))
print(test.run())
