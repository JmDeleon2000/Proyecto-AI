import time
import numpy as np
import pygame

pygame.init()

class conways:
    def __init__(self, size = 100, max_it = 100):
        self.max_it = max_it
        screen_size = (1024, 1024)
        self.liveCellColor = (255, 255, 255)
        self.deadCellColor = (25, 25, 25)
        self.screen = pygame.display.set_mode(screen_size)
        self.render = False

        self.x_size = size+2
        self.y_size = size+2
        self.x_bound = self.x_size - 1
        self.y_bound = self.y_size - 1

        self.square_off = int(screen_size[0]/(self.x_size-2))

        self.buff_1 = np.random.choice(
            a = [False, False, False, False, False, True, True], 
            size = (self.x_size, self.y_size))
        self.buff_2 = np.copy(self.buff_1)

        self.buff = []
        self.buff.append(self.buff_1)
        self.buff.append(self.buff_2)

        self.reset(self.buff_1)

    def reset(self, a, /, offset = True):
        if offset:
            self.moves = 0
            self.buff_1 = a

            self.buff[0] = self.buff_1
            self.buff[1] = self.buff_2
            for y in range(1, self.y_bound):
                for x in range(1, self.x_bound):
                    if self.buff_1[y, x]:
                        self.moves += 1
            #reset padding
            for x in range(self.x_size):
                self.buff_1[0, x] = False
                self.buff_1[x, 0] = False
                self.buff_1[self.y_bound, x] = False
                self.buff_1[x, self.y_bound] = False


            self.buff_2 = np.copy(self.buff_1)
        else:
            self.moves = 0
            #self.buff_1 = a

            self.buff[0] = self.buff_1
            self.buff[1] = self.buff_2
            for y in range(1, self.y_bound):
                for x in range(1, self.x_bound):
                    self.buff_1[y, x] = a[y-1, x-1]
                    if self.buff_1[y, x]:
                        self.moves += 1


            self.buff_2 = np.copy(self.buff_1)


    def run(self):
        for i in range(self.max_it):
            changed = False
            self.screen.fill(self.deadCellColor)

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
                        
                    if (self.buff[0][y, x] and count < 2 or count > 3):
                        self.buff[1][y, x] = False
                        changed = True
                    if self.render:
                        if self.buff[0][y, x]:
                            self.screen.fill(
                                self.liveCellColor, 
                                rect=(self.square_off*(y-1), self.square_off*(x-1), 
                                self.square_off, self.square_off))



            if self.render:
                pygame.display.flip()
            #time.sleep(1)
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
                            alive = True
                            break
                    if alive:
                        break
                if alive:
                    return float('inf')
                else:
                    return i**2 #+ self.moves
        return  self.max_it**2 #+ self.moves




#test = conways(size = 512, max_it=1000)
#print(test.run())
#
#x = np.zeros(shape=(514, 514), dtype=bool)
#x[100, 100] = True
#x[100, 101] = True
#x[101, 100] = True
#x[101, 101] = False
#
#
#test.reset(x)
#print(test.run())
#
#x[100, 100] = True
#x[100, 101] = True
#x[101, 100] = True
#x[101, 101] = True
#
#
#test.reset(x)
#print(test.run())