from itertools import combinations


def get_all_antennas(list_lines: list[str]) -> dict:
    """
    Get all antinodes
    """
    antinodes = {}
    max_x = len(list_lines[0])
    max_y = len(list_lines)
    for x in range(max_x):
        for y in range(max_y):
            char = list_lines[y][x]
            if char != ".":
                if char not in antinodes:
                    antinodes[char] = [(x, y)]
                else:
                    antinodes[char].append((x, y))
    return antinodes


def count_antinodes(list_lines: list[str]) -> int:
    """
    Count antinodes
    """
    max_x = len(list_lines[0])
    max_y = len(list_lines)
    dict_antennas = get_all_antennas(list_lines)
    set_antinodes = set()
    for char, list_tuple in dict_antennas.items():
        if len(list_tuple) < 2:
            print("Char: ", char, "is alone")
            continue
        all_combinations = list(combinations(list_tuple, 2))
        #print("Char: ", char, " List: ", list_tuple, " Combinations: ", len(all_combinations))
        for combination in all_combinations:
            X1 = combination[0]
            X2 = combination[1]
            X1X2 = get_vector(X1, X2)
            X2X1 = (-X1X2[0], -X1X2[1])
            #print("X1: ", X1, " X2: ", X2, " X1X2: ", X1X2, " X2X1: ", X2X1)
            X1 = add_vector(X1, X2X1)
            X2 = add_vector(X2, X1X2)
            #print("X1: ", X1, " X2: ", X2)
            while (check_tuple_in_map(X2, max_x, max_y, set_antinodes)):
                #print("Adding to set: ", X2)
                set_antinodes.add(X2)
                X2 = add_vector(X2, X1X2)
                #print("Tuple before test", X2)
            while (check_tuple_in_map(X1, max_x, max_y, set_antinodes)):
                set_antinodes.add(X1)
                X1 = add_vector(X1, X2X1)
    new_map = create_new_map(list_lines, set_antinodes)
    pretty_print(list_lines)
    print("\n\n")
    pretty_print(new_map)
    set_antinodes = add_antenna_to_set(set_antinodes, dict_antennas)
    print(count_not_empty_point(new_map))
    return len(set_antinodes)


def count_not_empty_point(list_lines: list[str]) -> int:
    """
    Count not empty point
    """
    count = 0
    for line in list_lines:
        for char in line:
            if char != ".":
                count += 1
    return count


def add_antenna_to_set(set_antinodes: set, dict_antennas: dict) -> set:
    """
    Add all antennas to set
    """
    for key, list_tuple in dict_antennas.items():
        if len(list_tuple) < 2:
            print("Char: ", key, "is alone")
            continue
        for tuple1 in list_tuple:
            set_antinodes.add(tuple1)
    return set_antinodes


def pretty_print(list_lines: list[str]):
    """
    Pretty print
    """
    for line in list_lines:
        print(line)


def create_new_map(list_lines: list[str], set_antinodes: set) -> list[str]:
    """
    Create new map
    """
    new_map = []
    max_x = len(list_lines[0])
    max_y = len(list_lines)
    for y in range(max_y):
        new_line = ""
        for x in range(max_x):
            if (x, y) in set_antinodes:
                new_line += "#"
            else:
                new_line += list_lines[y][x]
        new_map.append(new_line)
    return new_map


def add_vector(point: tuple[int, int], vector: tuple[int, int]) -> tuple[int, int]:
    """
    Add vector
    """
    return point[0] + vector[0], point[1] + vector[1]


def get_vector(point1: tuple[int, int], point2: tuple[int, int]) -> tuple[int, int]:
    """
    Get vector
    """
    return point2[0] - point1[0], point2[1] - point1[1]


def check_tuple_in_map(tuple1: tuple[int, int], max_x: int, max_y: int,
                       set_antinodes: set) -> bool:
    """
    Check tuple in map
    """
    if tuple1[0] < 0 or tuple1[0] >= max_x:
        return False
    if tuple1[1] < 0 or tuple1[1] >= max_y:
        return False
    if tuple1 in set_antinodes:
        return False
    return True


def get_input(file_path: str) -> list[str]:
    """
    Get input
    """
    list_lines: list[str] = []
    with open(file_path, "r") as file:
        for line in file:
            list_lines.append(line.strip())
    return list_lines


def work(file_path: str) -> int:
    """
    Work
    """
    list_lines = get_input(file_path)
    count = count_antinodes(list_lines)
    return count


def main():
    print("Hello World!")
    print(work("input.txt"))


if __name__ == "__main__":
    main()
