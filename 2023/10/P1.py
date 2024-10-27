import numpy as np
from typing import List, Tuple


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
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            if data[y, x] == "S":
                print("Found start at: ", x, y)
                return (x, y)
    return None


def find_first_cells(map2d: np.array) -> List[Tuple]:
    """
    Find cells that are valid
    """
    (sx, sy) = find_start(map2d)
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


def run_through_maze(map2d: np.array) -> int:
    """
    Run through and find furthest cell from start
    """
    (sx, sy) = find_start(map2d)
    count: int = 0
    count2: int = 0
    valid_first_cells = find_first_cells(map2d)
    active_cell1 = valid_first_cells[0]
    previous_cell1 = (sx, sy)
    active_cell2 = valid_first_cells[1]
    previous_cell2 = (sx, sy)
    while active_cell1 != (sx, sy) or active_cell2 != (sx, sy):
        print("cell1: ", active_cell1, ", cell2: ", active_cell2)
        count += 1
        active_cell1, previous_cell1 = get_next_cells(map2d, 
                                                    active_cell1, 
                                                    previous_cell1)
        count2 += 1
        active_cell2, previous_cell2 = get_next_cells(map2d, 
                                                    active_cell2, 
                                                    previous_cell2)
    return round((max(count, count2) + 1)/ 2)


def main():
    print("Hello")
    data_test1 = read_input("input_test1.txt")
    print(data_test1)
    data_test2 = read_input("input_test2.txt")
    assert(run_through_maze(data_test1) == 4)
    assert(run_through_maze(data_test2) == 8)
    data = read_input("input.txt")
    print(run_through_maze(data))


if __name__ == "__main__":
    main()
