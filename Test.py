import pygame

pygame.init()

maze = [    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 1, 1, 0]
            ]

rows = len(maze)
cols = len(maze[0])
cell_size = 50
WIDTH = cols*cell_size
HEIGHT = rows*cell_size




WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A star")


white = (255,255,255)
black = (0,0,0)



clock = pygame.time.Clock()
FPS = 60


def draw_maze(WIN, maze):
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == 1:
                color = black
            else:
                color = white
            pygame.draw.rect(WIN,color,(col*cell_size,row*cell_size,cell_size,cell_size),0)



if __name__ == '__main__':
    running = True
    draw_maze(WIN,maze)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            pygame.display.update()