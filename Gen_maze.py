import random

def random_generate_maze(rows, cols, wall_possibilities = 0.3):
    # 1 is blocked
    maze = [[1 if random.random() < wall_possibilities else 0 for _ in range(cols)] for _ in range(rows) ]

    maze[0][0] = 0
    maze[len(maze)-1][len(maze[0])-1] = 0

    return maze