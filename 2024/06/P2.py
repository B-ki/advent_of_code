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


def get_all_X_positions(array: np.array) -> list[list[int]]:
    """
    Get all 'X' positions in np.array
    """
    positions = []
    for y in range(array.shape[0]):
        for x in range(array.shape[1]):
            if array[y, x] == "X":
                positions.append([x, y])
    return positions


def stop_loop(array: np.array, x: int, y: int, direction: int,
              max_x: int, max_y: int) -> bool:
    if x < 0 or x >= max_x or y < 0 or y >= max_y:
        return True
    return False


def new_map_symbol(symbol: str, direction: int) -> str:
    if symbol == "+":
        return "+"
    if direction == UP:
        if symbol == "-":
            return "+"
        elif symbol == "d":
            return "|"
        else:
           return "u"
    elif direction == RIGHT:
        if symbol == "|":
            return "+"
        elif symbol == "l":
            return "-"
        else:
            return "r"
    elif direction == DOWN:
        if symbol == "-":
            return "+"
        elif symbol == "u":
            return "|"
        else:
            return "d"
    else:
        if symbol == "|":
            return "+"
        elif symbol == "r":
            return "-"
        else:
            return "l"


def test_all_obstacles(array: np.array, start: list[int]) -> int:
    clean_array = np.copy(array)
    count_loop = get_loop(array, start)
    positions = get_all_X_positions(array)
    clean_array[7, 7] = "#"
    print(array)
    print(clean_array)
    for position in positions:
        new_array = np.copy(clean_array)
        new_array[position[1], position[0]] = "#"
        count_loop += get_loop(new_array, start)
    return count_loop


def get_loop(array: np.array, start: list[int]) -> int:
    x = start[0]
    y = start[1]
    direction = start[2]
    max_x = array.shape[1]
    max_y = array.shape[0]
    count_x = 0
    while count_x < 100:
        print(array)
        if array[y, x] == "X":
            count_x += 1
        else:
            count_x = 0
        if check_last_cell(x, y, direction, max_x, max_y):
            array[y, x] = "X"
            return 0
        elif check_obstacle(array, x, y, direction) != -1:
            array[y, x] = "X"
            direction = check_obstacle(array, x, y, direction)
            x = get_next_x(x, direction)
            y = get_next_y(y, direction)
        else:
            array[y, x] = "X"
            x = get_next_x(x, direction)
            y = get_next_y(y, direction)
    print(array)
    return 1


def get_X_array(array: np.array, start: list[int]) -> np.array:
    print("Moving from", start)
    x = start[0]
    y = start[1]
    direction = start[2]
    max_x = array.shape[1]
    max_y = array.shape[0]
    count_x = 0
    while count_x < 1000:
        if array[y, x] == "X":
            count_x += 1
        else:
            count_x = 0
        if check_last_cell(x, y, direction, max_x, max_y):
            array[y, x] = "X"
            print(array)
            return array
        elif check_obstacle(array, x, y, direction) != -1:
            array[y, x] = "X"
            direction = check_obstacle(array, x, y, direction)
            x = get_next_x(x, direction)
            y = get_next_y(y, direction)
        else:
            array[y, x] = "X"
            x = get_next_x(x, direction)
            y = get_next_y(y, direction)
    return array


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
    print(test_all_obstacles(map_example, find_start(map_example)))
    #map_input = get_input("input.txt")
    #print(get_X_array(map_input, find_start(map_input)))


if __name__ == "__main__":
    main()
