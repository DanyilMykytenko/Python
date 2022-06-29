import pygame
import random
import sys, os
from pygame.locals import *
import time

RES = WIDTH, HEIGHT = 902, 602
TILE = 50
cols, rows = WIDTH // TILE, HEIGHT // TILE
pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
'''
def get_click_mouse_pos():
    x, y = pygame.mouse.get_pos()
    grid_x, grid_y * x // TILE + 1, y // TILE
    pygame.draw.rect(sc, pygame.Color('red'), get_rect(grid_x, grid_y))
    click = pygame.mouse.get_pressed()
    return (grid_x, grid_y) if click[0] else False

pause = False

def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]
'''
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw_current_cell(self, color):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(sc, pygame.Color(color), (x + 2, y + 2, TILE - 2, TILE - 2))

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            pygame.draw.rect(sc, pygame.Color('black'), (x, y, TILE, TILE))

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), 3)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), 3)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), 3)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), 3)

    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            return False
        return grid_cells[find_index(x, y)]

    def check_neighbours(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return random.choice(neighbors) if neighbors else False
    #testing
    def check_neighbours_for_exit(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            if top.walls['bottom'] == False: neighbors.append(top)
        if right and not right.visited:
            if right.walls['left'] == False: neighbors.append(right)
        if bottom and not bottom.visited:
            if bottom.walls['top'] == False: neighbors.append(bottom)
        if left and not left.visited:
            if left.walls['right'] == False: neighbors.append(left)
        #random.seed(random.randint(0,100))
        return random.choice(neighbors) if neighbors else False

def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2

def paused(event):
    #for event in pygame.event.get():
    if event.type==KEYUP:
        if event.key==K_p:
            pause = True
    #for event in pygame.event.get():
    elif event.type == KEYUP:
        if event.key == K_p:
            pause = True
            pause = paused()
    while pause == True:
        for event in pygame.event.get():
            if event.type==KEYUP:
                if event.key==K_p:
                    return False
                elif event.key == K_ESCAPE:
                    exit(0)

def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

def finding_any_exit(current_cell):
    path = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        current_cell.visited = True
        #current_cell.draw_current_cell('red')

        next_cell = current_cell.check_neighbours_for_exit()
        if next_cell:
            next_cell.visited = True
            path.append(current_cell)
            current_cell = next_cell
        else:
            if path:
                current_cell = path.pop()
            else:
                break
        if next_cell == grid_cells[-1]:
            break
    print(len(path))
    return path

def finding_best_exit():
    paths = []
    for i in range(10):
        way = finding_any_exit(grid_cells[0])
        reset_map()
        if way:
            paths.append(way)
    return min(paths, key=len).copy()

def reset_map():
    for cell in grid_cells:
        cell.visited = False

def generate_Labyrinth(current_cell):
    while True:
        sc.fill(pygame.Color('darkslategray'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        [cell.draw() for cell in grid_cells]
        current_cell.visited = True
        current_cell.draw_current_cell('saddlebrown')

        next_cell = current_cell.check_neighbours()
        if next_cell:
            next_cell.visited = True
            stack.append(current_cell)
            remove_walls(current_cell, next_cell)
            current_cell = next_cell
        else:
            if stack:
                current_cell = stack.pop()
            else:
                break

        pygame.display.flip()
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_p:
                    paused(event)
    

grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
#current_cell = grid_cells[int(input())]
current_cell = grid_cells[0]
stack = []
generate_Labyrinth(current_cell)
#dfs
best_path = finding_best_exit().copy()
grid_cells[-1].draw_current_cell('brown')
for cell in best_path:
    cell.draw_current_cell('red')
    pygame.display.update()
    pygame.display.flip()
    clock.tick(100)

time.sleep(10)