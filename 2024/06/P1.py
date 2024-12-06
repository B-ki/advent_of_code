import numpy as np


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def count_X(array: np.array) -> int:
    """
    Count 'X' in np.array
    """
    count = 0
    for y in range(array.shape[0]):
        for x in range(array.shape[1]):
            if array[y, x] == "X":
                count += 1
    return count


def move(array: np.array, start: list[int]) -> int:
    print("Moving from", start)
    x = start[0]
    y = start[1]
    direction = start[2]
    max_x = array.shape[1]
    max_y = array.shape[0]
    while x < max_x and 0 <= x and y < max_y and 0 <= y:
        if check_last_cell(x, y, direction, max_x, max_y):
            array[y, x] = "X"
            print(array)
            return count_X(array) 
        elif check_obstacle(array, x, y, direction) != -1:
            array[y, x] = "X"
            direction = check_obstacle(array, x, y, direction)
            x = get_next_x(x, direction)
            y = get_next_y(y, direction)
        else:
            array[y, x] = "X"
            x = get_next_x(x, direction)
            y = get_next_y(y, direction)
    return 0


def get_next_x(x: int, direction) -> int:
    """
    Get next x coordinate
    """
    if direction == RIGHT:
        return x + 1
    elif direction == LEFT:
        return x - 1
    return x


def get_next_y(y: int, direction) -> int:
    """
    Get next y coordinate
    """
    if direction == DOWN:
        return y + 1
    elif direction == UP:
        return y - 1
    return y

def check_obstacle(array: np.array, x: int, y: int, direction: int) -> int:
   if direction == UP and array[y - 1, x] == "#":
       return RIGHT
   elif direction == RIGHT and array[y, x + 1] == "#":
       return DOWN
   elif direction == DOWN and array[y + 1, x] == "#":
       return LEFT
   elif direction == LEFT and array[y, x - 1] == "#":
       return UP
   return -1


def check_last_cell(x: int, y: int, direction: int,
                    max_x: int, max_y: int) -> bool:
    """
    Check if last cell
    """
    if x == 0 and direction == LEFT:
        return True
    elif x == max_x - 1 and direction == RIGHT:
        return True
    elif y == 0 and direction == UP:
        return True
    elif y == max_y - 1 and direction == DOWN:
        return True
    return False


def get_direction(symbol: str) -> int:
    """
    Get direction from symbol
    """
    if symbol == "^":
        return UP
    elif symbol == ">":
        return RIGHT
    elif symbol == "v":
        return DOWN
    elif symbol == "<":
        return LEFT
    else:
        return -1


def find_start(map: np.array) -> list[int]:
    """
    Find cell "^" (unique)
    """
    for y in range(map.shape[0]):
        for x in range(map.shape[1]):
            if map[y,x] == "^":
                return [x, y, get_direction(map[y][x])]


def get_input(file_path: str) -> np.array:
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())
        return np.array([list(line) for line in lines])


def main():
    print("Hello, World!")
    map_example = get_input("example.txt")
    print(move(map_example, find_start(map_example)))
    map_input = get_input("input.txt")
    print(move(map_input, find_start(map_input)))


if __name__ == "__main__":
    main()
