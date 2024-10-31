import numpy as np
from typing import List, Tuple


class colors:
    GREEN = '\033[92m'
    END = '\033[0m'
    RED = '\033[91m'


def pretty_print(data: np.array):
    """
    Pretty print the maze
    """
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i, j] == "0":
                print(colors.RED + data[i, j] + colors.END, end = " ")
            elif data[i, j] == "X":
                print(colors.GREEN + data[i, j] + colors.END, end = " ")
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
    print(data.shape)
    for x in range(data.shape[1]):
        for y in range(data.shape[0]):
            if data[y, x] == "S":
                print("Found start at: ", x, y)
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
    print_data = False
    if color == "0":
        print_data = True
    if map2d[y, x] == color or map2d[y, x] == '0':
        if print_data:
            print("Cell: ", x, y, " is colored by 0 already")
        return False
    if (x, y) in list_boundary:
        if print_data:
            print("Cell: ", x, y, " is a boundary")
        return False
    if print_data:
        print("Cell: ", x, y, " is inside")
    return True


def flood_fill(map2d: np.array, boundaries: List[Tuple], 
               color: str, start_cell: Tuple) -> int:
    """
    Flood fill the maze
    """
    if not inside(start_cell, map2d, boundaries, color):
        return 0
    map2d[start_cell[1], start_cell[0]] = color
    cell_inside = []
    stack = []
    stack.append(start_cell)
    while len(stack) > 0:
        (x, y) = stack.pop()
        nx = x
        while nx - 1 >= 0 and inside((nx - 1, y), map2d, boundaries, color):
            cell_inside.append((nx - 1, y))
            map2d[y, nx - 1] = color
            nx = nx - 1
        while x <= map2d.shape[1] and inside((x, y), map2d, boundaries, color):
            cell_inside.append((x, y))
            map2d[y, x] = color
            x = x + 1
            stack = scan(nx, x - 1, y + 1, stack, map2d, boundaries, color)
            stack = scan(nx, x - 1, y - 1, stack, map2d, boundaries, color)
    return len(cell_inside)


def scan(lx: int, rx: int, y: int, stack: List[Tuple], 
         map2d: np.array, color: str, boundaries: List[Tuple]) -> List[Tuple]:
    cell_added = False
    for x in range(lx, rx):
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
    return boundaries


def run_through_maze(map2d: np.array) -> int:
    """
    Run through the maze
    """
    boundaries = get_boundaries(map2d)
    for i in range(map2d.shape[1]):
        flood_fill(map2d, boundaries, "0", (i, 0))
        flood_fill(map2d, boundaries, "0", (i, map2d.shape[0] - 1))
    for j in range(map2d.shape[0]):
        flood_fill(map2d, boundaries, "0", (0, j))
        flood_fill(map2d, boundaries, "0", (map2d.shape[1] - 1, j))
    print("After filling with 0")
    pretty_print(map2d)
    count = 0
    for i in range(map2d.shape[1]):
        for j in range(map2d.shape[0]):
            if map2d[j, i] != "0" and (i, j) not in boundaries:
                count += flood_fill(map2d, boundaries, "X", (i, j))
    print("After filling with X")
    pretty_print(map2d)
    # count value like "X" in map2d
    count = np.count_nonzero(map2d == "X")
    return count


def main():
    print("Hello")
    data_test1 = read_input("input_test1.txt")
    print("Data test 1 :")
    pretty_print(data_test1)
    print(run_through_maze(data_test1))
    data_test2 = read_input("input_test2.txt")
    print("Data test 2 :")
    pretty_print(data_test2)
    print(run_through_maze(data_test2))
    data_test3 = read_input("input3.txt")
    print("Data test 3 :")
    pretty_print(data_test3)
    print(run_through_maze(data_test3))
    #data = read_input("input.txt")
    #print(run_through_maze(data))


if __name__ == "__main__":
    main()
