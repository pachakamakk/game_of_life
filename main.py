import sys
from time import sleep
from random import randrange

def init_world(world, size, proportion):
    total_cell = (size * size) / proportion
    iterator = range(size)
    for x in iterator:
        for y in iterator:
            world[x][y] = 0
    for i in range(total_cell):
        while True:
            pos_x = randrange(0, size, 1)
            pos_y = randrange(0, size, 1)
            if (world[pos_x][pos_y] == 0):
                world[pos_x][pos_y] = 1
                break

def dump_world(world):
    for line in world:
        for elem in line:
            sys.stdout.write(str(elem))
        sys.stdout.write("\n")
    print "\n\n\n"
            
def check_neighbors(world, size, x, y):
    cells = 0
    if (x != 0):
        if (world[x - 1][y] == 1):
            cells += 1
        if (y != 0):
            if (world[x - 1][y - 1] == 1):
                cells += 1
        if (y != size - 1):
            if (world[x - 1][y + 1] == 1):
                cells += 1
    if (x != size - 1):
        if (world[x + 1][y] == 1):
            cells += 1
        if (y != 0):
            if (world[x + 1][y - 1] == 1):
                cells += 1
        if (y != size - 1):
            if (world[x + 1][y + 1]):
                cells += 1
    if (y != 0):
        if (world[x][y - 1] == 1):
            cells += 1
    if (y != size - 1):
        if (world[x][y + 1] == 1):
            cells += 1
    return cells
    
def life(world, size):
    coords = []
    iterator = range(size)
    for x in iterator:
        for y in iterator:
            if (world[x][y] == 0):
                if (check_neighbors(world, size, x, y) == 3):
                    world[x][y] = 2
                    coords.append([x, y])
            elif (world[x][y] == 1):
                neighbors = check_neighbors(world, size, x, y)
                if (neighbors < 2 or neighbors > 3):
                    world[x][y] = 0
    for elem in coords:
        world[elem[0]][elem[1]] = 1

size = 32
proportion = 3

while True:
    world = [[0 for x in range(size)] for y in range(size)]
    init_world(world, size, proportion)
    while True:
        dump_world(world)
        life(world, size)
        sleep(1)
    break
