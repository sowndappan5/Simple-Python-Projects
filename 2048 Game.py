import random

def init_game():
    grid = [[0 for _ in range(4)] for _ in range(4)]
    print("Commands: 'W'/'w' - Up, 'S'/'s' - Down, 'A'/'a' - Left, 'D'/'d' - Right")
    add_new_2(grid)
    return grid

def add_new_2(grid):
    while True:
        r, c = random.randint(0, 3), random.randint(0, 3)
        if grid[r][c] == 0:
            grid[r][c] = 2
            break

def get_state(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return 'WON'
            if grid[i][j] == 0:
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]:
                return 'GAME NOT OVER'
    for j in range(3):
        if grid[3][j] == grid[3][j+1]:
            return 'GAME NOT OVER'
    for i in range(3):
        if grid[i][3] == grid[i+1][3]:
            return 'GAME NOT OVER'
    return 'LOST'

def compress(grid):
    changed = False
    new_grid = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_grid, changed

def merge(grid):
    changed = False
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j+1] = 0
                changed = True
    return grid, changed

def reverse(grid):
    return [row[::-1] for row in grid]

def transpose(grid):
    return [list(row) for row in zip(*grid)]

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    return new_grid, changed

def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed