from PriorityQueue import PriorityQueue
from Heuristic import cal_heuristics
import pygame
from Gen_maze import random_generate_maze

pygame.init()
# 1 is blocked
# grid = [    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
#             [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
#             [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#             [0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
#             [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
#             [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#             [0, 0, 0, 1, 1, 1, 0, 1, 1, 0]
#             ]
grid = random_generate_maze(65,120)

delay_time = 2              # delay time of pygame
rows = len(grid)
cols = len(grid[0])
WIDTH = 1200
HEIGHT = 650
cell_size = 10



WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A star")


white = (255,255,255)
black = (0,0,0)
cyan  = (0,255,229) # start color
red   = (255,0,0)   # dest color
blue  = (0,8,255)   # close color
green = (0,255,85)  # open color
yellow= (245,255,0) #path color
dark_red = (125,0,0)

text_size = int(cell_size*9/35)
Font = pygame.font.Font(None,text_size)


def draw_maze(WIN, maze):
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == 1:
                color = black
            else:
                color = white
            pygame.draw.rect(WIN,color,(col*cell_size,row*cell_size,cell_size,cell_size),0)

def draw_cell(WIN, cell, text, bg_color, text_color = black):
    pygame.draw.rect(WIN, bg_color, (cell[1]*cell_size, cell[0]*cell_size, cell_size, cell_size),0)
    ##
    text_surface = Font.render(text[0],True,text_color)
    #text_width, text_height = text_surface.get_size()
    #text_position = ((cell[1]*cell_size - text_height)//2, (cell[0]*cell_size - text_width)//2)
    text_position = (cell[1]*cell_size, cell[0]*cell_size)
    WIN.blit (text_surface, text_position)
    ##
    text_surface = Font.render(text[1],True,text_color)
    text_position = (cell[1]*cell_size, cell[0]*cell_size + text_size)
    WIN.blit (text_surface, text_position)
    ##
    text_surface = Font.render(text[2],True,text_color)
    text_position = (cell[1]*cell_size, cell[0]*cell_size + 2*text_size)
    WIN.blit (text_surface, text_position)
    ##
    text_surface = Font.render(text[3],True,text_color)
    text_position = (cell[1]*cell_size, cell[0]*cell_size + 3*text_size)
    WIN.blit (text_surface, text_position)


    pygame.display.update((cell[1]*cell_size, cell[0]*cell_size, cell_size, cell_size))



#################################################




class Cell:
    def __init__(self):
        self.g = float("inf")
        self.f = float("inf")
        self.h = 0.0
        self.parent = [0,0]

def is_wall(grid, cell_coord):
    return grid[cell_coord[0]][cell_coord[1]] == 1

def out_of_grid(grid_row, grid_col, cell_coord):
    return cell_coord[0] < 0 or  cell_coord[0] >= grid_row or  cell_coord[1] < 0 or  cell_coord[1] >= grid_col

def is_destination(cell_coord, dest):
    return cell_coord[0] == dest[0] and cell_coord[1] == dest[1]

def trace_path(grid_infor, start, dest):
    path = []
    current = dest
    while current != start:
        path.append(current)
        current = grid_infor[current[0]][current[1]].parent
    path.append(current)
    path.reverse()
    ##pygame##
    for cell in path:
        draw_cell(WIN,cell,detail_cell(grid_infor,cell),yellow)

    draw_cell(WIN,start,detail_cell(grid_infor,start),cyan)
    draw_cell(WIN,dest,detail_cell(grid_infor,dest),dark_red)
    print(len(path))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    #########
    return path

def detail_cell(grid_infor, cell):
    g = round(grid_infor[cell[0]][cell[1]].g, 2)
    h = round(grid_infor[cell[0]][cell[1]].h, 2)
    f = round(grid_infor[cell[0]][cell[1]].f, 2)
    parent = grid_infor[cell[0]][cell[1]].parent
    return [str(g),str(h),str(f),str(parent)]


def Astar(grid,start, dest, num_directional_offset = 8):
    if num_directional_offset == 8:
        cal_distance_method = "Euclid"
        directional_offset = [
            (-1,0), #up
            (1,0),  #down
            (0,-1), #left
            (0,1),  #right
            (-1,-1),#top-left
            (-1,1), #top-right
            (1,-1), #bottom-left
            (1,1),  #bottom-right
        ]

    elif num_directional_offset == 4:
        choose = 2 #int(input("Choose: 1 - Euclid; 2 - Manhattan:  "))
        if choose == 1:
            cal_distance_method = "Euclid"
        elif choose == 2:
            cal_distance_method = "Manhattan"
        directional_offset = [
            (-1,0), #up
            (1,0),  #down
            (0,-1), #left
            (0,1),  #right
        ] 

    GRID_ROW = len(grid)
    GRID_COL = len(grid[1])
    grid_infor = [[Cell() for i in range(GRID_COL)] for j in range(GRID_ROW)]
    grid_infor [start[0]][start[1]].g = 0.0
    grid_infor [start[0]][start[1]].h = cal_heuristics(start,dest,cal_distance_method)
    grid_infor [start[0]][start[1]].f = grid_infor [start[0]][start[1]].g + grid_infor [start[0]][start[1]].h
    is_close_cell = [[False for i in range(GRID_COL)] for j in range(GRID_ROW)]



    if is_wall(grid, dest):
        return "Dest is wall"
    
    if out_of_grid(GRID_ROW, GRID_COL, dest):
        return "Destination is out of grid"
    
    if is_wall(grid, start):
        return "Start is wall"
    
    if out_of_grid(GRID_ROW, GRID_COL, start):
        return "Start is out of grid"
        
    if is_destination(start, dest):
        return "Start is destination: " + str([start])
    

    open_list = PriorityQueue()
    open_list.push((0.0,start)) # add start to open_list with f_start is 0


    draw_maze(WIN,grid)
    pygame.display.update()
    draw_cell(WIN,start,detail_cell(grid_infor,start),cyan)
    draw_cell(WIN,dest,detail_cell(grid_infor,dest),red)


    while not open_list.isEmpty():
        ##pygame###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ###########


        #print (open_list)
        current_cell = open_list.pop()[1] # get the coordinate of cell with smallest h
        is_close_cell[current_cell[0]][current_cell[1]] = True # set current_cell is close
        ##print (current_cell)
        draw_cell(WIN,current_cell,detail_cell(grid_infor, current_cell),blue)
        draw_cell(WIN,start,detail_cell(grid_infor,start),cyan)

        for direction in directional_offset:
            next_cell = [current_cell[0] + direction[0], current_cell[1] + direction[1]]
            if (not out_of_grid(GRID_ROW, GRID_COL, next_cell)) and (not is_wall(grid, next_cell)) and (not is_close_cell[next_cell[0]][next_cell[1]]) :
                ##print (next_cell)
                if is_destination(next_cell,dest):
                    draw_cell(WIN,dest,detail_cell(grid_infor,dest),dark_red)
                    grid_infor[next_cell[0]][next_cell[1]].parent = current_cell
                    return trace_path(grid_infor, start, dest)
                
                else:
                    g_new_next_cell = grid_infor[current_cell[0]][current_cell[1]].g + 1.0
                    h_new_next_cell = cal_heuristics(next_cell,dest,cal_distance_method)
                    f_new_next_cell = g_new_next_cell + h_new_next_cell
                    ##print((g_new_next_cell, h_new_next_cell, f_new_next_cell))
                    if grid_infor[next_cell[0]][next_cell[1]].f == float("inf") or f_new_next_cell < grid_infor[next_cell[0]][next_cell[1]].f:
                        # add next_cell to open_list or update if it was in open list
                        open_list.push((f_new_next_cell,next_cell))
                        grid_infor[next_cell[0]][next_cell[1]].parent = current_cell
                        grid_infor[next_cell[0]][next_cell[1]].g = g_new_next_cell
                        grid_infor[next_cell[0]][next_cell[1]].h = h_new_next_cell
                        grid_infor[next_cell[0]][next_cell[1]].f = f_new_next_cell
                        # draw next_cell
                        draw_cell(WIN,next_cell,detail_cell(grid_infor,next_cell),green)

        pygame.time.delay(delay_time)

    return "Cannot finding !!!"

if __name__ == "__main__":
        print (Astar(grid, [rows-1,cols-1], [0,0],4))