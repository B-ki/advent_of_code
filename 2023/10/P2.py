import numpy as np
from typing import List, Tuple
import pdb;


class colors:
    GREEN = '\033[92m'
    END = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def pretty_print(data: np.array, boundary: List[Tuple] = None):
    """
    Pretty print the maze
    """
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i, j] == "0":
                print(colors.RED + data[i, j] + colors.END, end = " ")
            elif data[i, j] == "X":
                print(colors.GREEN + data[i, j] + colors.END, end = " ")
            elif boundary is not None and (j, i) in boundary:
                print(colors.BLUE + data[i, j] + colors.END, end = " ")
            else:
                print(data[i, j], end = " ")
        print("")


def read_input(file_path: str) -> np.array:
    """
    Transform the input file into a numpy array, each char is a value
    """
    with open(file_path, "r") as f:
       data = f.readlines()
    data = [list(i.strip()) for i in data]
    return np.array(data)


def find_start(data: np.array) -> tuple:
    """
    Find the starting point of the maze    """
    for x in range(data.shape[1]):
        for y in range(data.shape[0]):
            if data[y, x] == "S":
                return (x, y)
    return None


def find_first_cells(map2d: np.array, sx: int, sy: int) -> List[Tuple]:
    """
    Find cells that are valid
    """
    valid_first_cells = []
    if map2d[sy, sx + 1] == '-' or map2d[sy, sx + 1] == 'J' or map2d[sy, sx + 1] == '7':
        valid_first_cells.append((sx + 1, sy))
    if map2d[sy, sx - 1] == '-' or map2d[sy, sx - 1] == 'F' or map2d[sy, sx - 1] == 'L':
        valid_first_cells.append((sx - 1, sy))
    if map2d[sy + 1, sx] == '|' or map2d[sy + 1, sx] == 'L' or map2d[sy + 1, sx] == 'J':
        valid_first_cells.append((sx, sy + 1)) 
    if map2d[sy - 1, sx] == '|' or map2d[sy - 1, sx] == 'F' or map2d[sy - 1, sx] == '7':
        valid_first_cells.append((sx, sy - 1))
    return valid_first_cells


def get_next_cells(map2d: np.array, cell: tuple, previous_cell: tuple) -> List[Tuple]:
    """
    Get the next cell
    """
    (x, y) = cell
    (px, py) = previous_cell
    (nx, ny) = (0, 0)
    if map2d[y, x] == '-':
        if x < px:
            (nx, ny) = (x - 1, y)
        else:
            (nx, ny) = (x + 1, y)
    elif map2d[y, x] == '|':
        if y < py:
            (nx, ny) = (x, y - 1)
        else:
            (nx, ny) = (x, y + 1)
    elif map2d[y, x] == 'J':
        if x > px:
            (nx, ny) = (x, y - 1)
        else:
            (nx, ny) = (x - 1, y)
    elif map2d[y, x] == 'L':
        if x < px:
            (nx, ny) = (x, y - 1)
        else:
            (nx, ny) = (x + 1, y)
    elif map2d[y, x] == 'F':
        if x < px:
            (nx, ny) = (x, y + 1)
        else:
            (nx, ny) = (x + 1, y)
    else: #if map2d[y, x] == '7':
        if x > px:
            (nx, ny) = (x, y + 1)
        else:
            (nx, ny) = (x - 1, y)
    return [(nx, ny), (x, y)]


def inside(cell: tuple, map2d: np.array, list_boundary: List[Tuple], 
           color: str) -> bool:
    (x, y) = cell
    if map2d[y, x] == color or map2d[y, x] == '0':
        return False
    if tuple_in_list((x, y), list_boundary):
        return False
    return True


def flood_fill(map2d: np.array, boundaries: List[Tuple], 
               color: str, start_cell: Tuple) -> int:
    """
    Flood fill the maze
    """
    if not inside(start_cell, map2d, boundaries, color):
        return 0
    cell_inside = [start_cell]
    stack = []
    stack.append(start_cell)
    while len(stack) > 0:
        (x, y) = stack.pop()
        nx = x
        while nx - 1 >= 0 and inside((nx - 1, y), map2d, boundaries, color):
            cell_inside.append((nx - 1, y))
            map2d[y, nx - 1] = color
            nx = nx - 1
        while x < map2d.shape[1] and inside((x, y), map2d, boundaries, color):
            cell_inside.append((x, y))
            map2d[y, x] = color
            x = x + 1
            if x - 1 > 0 and y + 1 < map2d.shape[0]:
                stack = scan(nx, x - 1, y + 1, stack, map2d, boundaries, color)
            if x - 1 > 0 and y - 1 > 0:
                stack = scan(nx, x - 1, y - 1, stack, map2d, boundaries, color)
    return len(cell_inside)


def flood_fill2(map2d: np.array, boundaries: List[Tuple],
                color: str, start_cell: Tuple) -> int:
    """
    Flood fill 2
    """
    if not inside(start_cell, map2d, boundaries, color):
        return 0
    cell_inside = []
    stack = []
    stack.append(start_cell)
    while len(stack) > 0:
        (x, y) = stack.pop()
        if inside((x, y), map2d, boundaries, color):
            cell_inside.append((x, y))
            map2d[y, x] = color
            if x - 1 > 0 and y < map2d.shape[0]:
                stack.append((x - 1, y))
            if x + 1 < map2d.shape[1] and y < map2d.shape[0]:
                stack.append((x + 1, y))
            if x < map2d.shape[1] and y - 1 > 0:
                stack.append((x, y - 1))
            if x < map2d.shape[1] and y + 1 < map2d.shape[0]:
                stack.append((x, y + 1))
    return len(cell_inside)


def tuple_in_list(t: Tuple, l: List[Tuple]) -> bool:
    """
    Check if a tuple is in a list of tuple_in_list
    """
    for i in l:
        if i == t:
            return True
    return False


def scan(lx: int, rx: int, y: int, stack: List[Tuple], 
         map2d: np.array, color: str, boundaries: List[Tuple]) -> List[Tuple]:
    """
    Scan the line
    """
    cell_added = False
    for x in range(lx, rx):
        #print("Scan: ", x, y)
        if not inside((x, y), map2d, boundaries, color):
            cell_added = False
        elif not cell_added:
            stack.append((x, y))
            cell_added = True
    return stack


def get_boundaries(map2d: np.array) -> List[Tuple]:
    """
    Get the boundaries of the maze
    """
    (sx, sy) = find_start(map2d)
    valid_first_cells = find_first_cells(map2d, sx, sy)
    cell = valid_first_cells[0]
    prev_cell = (sx, sy)
    boundaries = []
    boundaries.append((sx, sy))
    while cell != (sx, sy):
        boundaries.append(cell)
        cell, prev_cell = get_next_cells(map2d, cell, prev_cell)
    #print("Boundaries: ", boundaries)
    return boundaries


def run_through_maze(map2d: np.array) -> int:
    """
    Run through the maze
    """
    boundaries = get_boundaries(map2d)
    for i in range(map2d.shape[1]):
        flood_fill2(map2d, boundaries, "0", (i, 0))
        flood_fill2(map2d, boundaries, "0", (i, map2d.shape[0] - 1))
    for j in range(map2d.shape[0]):
        flood_fill2(map2d, boundaries, "0", (0, j))
        flood_fill2(map2d, boundaries, "0", (map2d.shape[1] - 1, j))
    count = 0
    for i in range(map2d.shape[1]):
        for j in range(map2d.shape[0]):
            if map2d[j, i] != "0" and (i, j) not in boundaries:
                count += flood_fill2(map2d, boundaries, "X", (i, j))
    return count


def widden_map(map2d: np.array, boundaries) -> np.array:
    """
    Widden the map by adding a . between each cell, row and column.
    For exampe :
    F--S
    L--J
    will become :
    F-----S
    |.....|
    L-----J
    """
    new_map = np.empty((map2d.shape[0] * 2 - 1, map2d.shape[1] * 2 - 1), dtype = str)
    new_map.fill(".")
    for x in range(map2d.shape[1]):
        for y in range(map2d.shape[0]):
            new_map[2 * y, 2 * x] = map2d[y, x]
    previous_cell = boundaries[0]
    for(x, y) in boundaries[1:]:
        if x == previous_cell[0]:
            new_map[max(y, previous_cell[1]) * 2 - 1, 2 * x] = "|"
        else:
            new_map[2 * y, max(x, previous_cell[0]) * 2 - 1] = "-"
        previous_cell = (x, y)
    start_cell = boundaries[0]
    last_cell = boundaries[-1]
    if start_cell[0] == last_cell[0]:
        new_map[max(last_cell[1], start_cell[1]) * 2 - 1, 
                2 * start_cell[0]] = "|"
    else:
        new_map[2 * start_cell[1], 
                2 * max(last_cell[0], start_cell[0]) - 1] = "-"
    return new_map 


def return_map_to_normal(map2d: np.array) -> np.array:
    """
    Inverse of widden_map
    """
    new_map = np.empty((map2d.shape[0] // 2 + 1, map2d.shape[1] // 2 + 1), dtype = str)
    new_map.fill(".")
    for x in range(new_map.shape[1]):
        for y in range(new_map.shape[0]):
            new_map[y, x] = map2d[2 * y, 2 * x]
    return new_map


def exploit_input(map2d: np.array) -> int:
    """ 
    Exploit the input
    """
    boundaries = get_boundaries(map2d)
    wide_map = widden_map(map2d, boundaries)
    pretty_print(wide_map)
    count = run_through_maze(wide_map)
    pretty_print(wide_map)
    normal_map = return_map_to_normal(wide_map)
    pretty_print(normal_map)
    count = np.count_nonzero(normal_map == "X")
    print("### Count: ", count, " ###")
    return count


def main():
    print("Hello")
    print("Data test 4 :")
    exploit_input(read_input("input4.txt"))
    print("Data test 3 :")
    exploit_input(read_input("input3.txt"))
    print("Normal input :")
    exploit_input(read_input("input.txt"))


if __name__ == "__main__":
    main()
