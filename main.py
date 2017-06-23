import sys

import pygame
from pygame.locals import *
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

def dump_world(world, iterator, sprite_cell, backgroud, window):
    window.blit(background, (0, 0))
    for x in iterator:
        for y in iterator:
            if (world[x][y] == 1):
                window.blit(sprite_cell, ((x) * 32, (y) * 32)) 
    pygame.display.flip()
            
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

size = 18
proportion = 3

pygame.init()
window =  pygame.display.set_mode((600, 600))
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((0,0,0))
sprite_cell = pygame.image.load("./ressources/cell.png").convert_alpha()
sprite_cell.set_colorkey((255, 0, 255))
window.blit(background,(0,0))
while True:
    iterator = range(size)
    world = [[0 for x in iterator] for y in iterator]
    init_world(world, size, proportion)
    while True:
        dump_world(world, iterator, sprite_cell, background, window)
        life(world, size)
        sleep(1)
    break
