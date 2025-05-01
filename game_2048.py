from kandinsky import *
from random import *
from ion import *
from time import *

def initialize_grid():
    grid = [[0, 0, 0, 0] for _ in range(4)]
    while sum(row.count(2) for row in grid) < 2:
        grid[randint(0, 3)][randint(0, 3)] = 2
    return grid

def move(grid, dir) :
    points = 0
    new_grid = []
    for _ in range(dir) :
        grid = [[grid[i][j] for i in range(3,-1,-1)] for j in range(4)]
    for row in grid:
        tiles = [tile for tile in row if tile != 0]
        for i in range(len(tiles) - 1):
            if tiles[i] == tiles[i + 1]:
                tiles[i] *= 2
                tiles[i + 1] = 0
                points += tiles[i]
        tiles = [tile for tile in tiles if tile != 0]
        new_grid.append(tiles + [0] * (4 - len(tiles)))
    for _ in range(4-dir) :
        new_grid = [[new_grid[i][j] for i in range(3,-1,-1)] for j in range(4)]
    return points, new_grid

def add_new_2(grid):
    i, j = randint(0, 3), randint(0, 3)
    while grid[i][j] != 0:
        i, j = randint(0, 3), randint(0, 3)
    grid[i][j] = 2 if randint(1, 4) != 4 else 4
    return grid

def over(grid):
    if all(grid == move(grid,k) for k in range(4)) :
        return True
    return False

def show(grid, turns, points) :
  fill_rect(0,0,300,300,color(255,255,255))
  for i in range(5) :
    fill_rect(70,200-i*40,201,1,color(0,0,0))
  for i in range(5) :
    fill_rect(70+i*50,40,1,161,color(0,0,0))
  for i in range(4) :
    for j in range(4) :
      draw_string(str(grid[i][j]),95+j*50-5*len(str(grid[i][j])),55+i*40)
  draw_string("Score : "+str(points),10,10)
  draw_string("Tour : "+str(turns),200,10)

def turn(grid):
    new_grid = grid
    while new_grid == grid:
        if keydown(KEY_UP) :
            points, new_grid = move(grid,3)
        elif keydown(KEY_DOWN) :
            points, new_grid = move(grid,1)
        elif keydown(KEY_LEFT) :
            points, new_grid = move(grid,0)
        elif keydown(KEY_RIGHT) :
            points, new_grid = move(grid,2)
    return points, add_new_2(new_grid)

def main():
    global points
    grid = initialize_grid()
    turns = 0
    score = 0
    while True:
        show(grid, turns, score)
        points, grid = turn(grid)
        score += points
        if over(grid):
            break
        turns += 1
        sleep(0.2)
    show(grid, turns, score)
    print("\nGAME OVER")

main()
