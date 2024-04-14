def Euclidean_Distance(cell_coord, dest):
    return ((cell_coord[0] - dest[0])**2 + (cell_coord[1] - dest[1])**2)**0.5

def Manhattan_Distance(cell_coord, dest):
    return abs(cell_coord[0] - dest[0]) + abs(cell_coord[1] - dest[1])

def cal_heuristics(cell_coord, dest, cal_distance_method):
    if cal_distance_method == "Manhattan":
        return Manhattan_Distance(cell_coord, dest)
    elif cal_distance_method == "Euclid":
        return Euclidean_Distance(cell_coord, dest)
    