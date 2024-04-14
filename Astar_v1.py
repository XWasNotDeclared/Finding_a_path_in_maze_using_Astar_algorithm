from PriorityQueue import PriorityQueue


class Cell:
    def __init__(self):
        self.g = float("inf")
        self.f = float("inf")
        self.h = 0
        self.parent = [0,0]

def is_wall(grid, cell_coord):
    return grid[cell_coord[0]][cell_coord[1]] == 1

def out_of_grid(grid_row, grid_col, cell_coord):
    return cell_coord[0] < 0 or  cell_coord[0] >= grid_row or  cell_coord[1] < 0 or  cell_coord[1] >= grid_col

def is_destination(cell_coord, dest):
    return cell_coord[0] == dest[0] and cell_coord[1] == dest[1]

def Euclidean_Distance(cell_coord, dest):
    return ((cell_coord[0] - dest[0])**2 + (cell_coord[1] - dest[1])**2)**0.5

def trace_path(grid_infor, start, dest):
    path = []
    current = dest
    while current != start:
        path.append(current)
        current = grid_infor[current[0]][current[1]].parent
    path.append(current)
    path.reverse()
    return path

def Astar(grid,start, dest):
    GRID_ROW = len(grid)
    GRID_COL = len(grid[1])
    grid_infor = [[Cell() for i in range(GRID_COL)] for j in range(GRID_ROW)]
    grid_infor [start[0]][start[1]].g = 0.0
    grid_infor [start[0]][start[1]].h = Euclidean_Distance(start, dest)
    grid_infor [start[0]][start[1]].f = grid_infor [start[0]][start[1]].g + grid_infor [start[0]][start[1]].h
    is_close_cell = [[False for i in range(GRID_COL)] for j in range(GRID_ROW)]
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



    while not open_list.isEmpty():
        print (open_list)
        current_cell = open_list.pop()[1] # get the coordinate of cell with smallest h
        is_close_cell[current_cell[0]][current_cell[1]] = True # set current_cell is close
        ##print (current_cell)

        for direction in directional_offset:
            next_cell = [current_cell[0] + direction[0], current_cell[1] + direction[1]]
            if (not out_of_grid(GRID_ROW, GRID_COL, next_cell)) and (not is_wall(grid, next_cell)) and (not is_close_cell[next_cell[0]][next_cell[1]]) :
                ##print (next_cell)
                if is_destination(next_cell,dest):
                    grid_infor[next_cell[0]][next_cell[1]].parent = current_cell
                    return trace_path(grid_infor, start, dest)
                
                else:
                    g_new_next_cell = grid_infor[current_cell[0]][current_cell[1]].g + 1.0
                    h_new_next_cell = Euclidean_Distance(next_cell,dest)
                    f_new_next_cell = g_new_next_cell + h_new_next_cell
                    ##print((g_new_next_cell, h_new_next_cell, f_new_next_cell))
                    if grid_infor[next_cell[0]][next_cell[1]].f == float("inf") or f_new_next_cell < grid_infor[next_cell[0]][next_cell[1]].f:
                        # add next_cell to open_list or update if it was in open list
                        open_list.push((f_new_next_cell,next_cell))
                        grid_infor[next_cell[0]][next_cell[1]].parent = current_cell
                        grid_infor[next_cell[0]][next_cell[1]].g = g_new_next_cell
                        grid_infor[next_cell[0]][next_cell[1]].h = h_new_next_cell
                        grid_infor[next_cell[0]][next_cell[1]].f = f_new_next_cell
    return "Cannot finding !!!"

if __name__ == "__main__":
    # 1 is blocked
    grid = [
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 1, 1, 0]
    ]
    print (Astar(grid, [8,0], [0,0]))