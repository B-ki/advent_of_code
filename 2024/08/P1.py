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
    count = 0
    max_x = len(list_lines[0])
    max_y = len(list_lines)
    dict_antennas = get_all_antennas(list_lines)
    set_antinodes = set()
    for char, list_tuple in dict_antennas.items():
        all_combinations = list(combinations(list_tuple, 2))
        for combination in all_combinations:
            x1, y1 = combination[0]
            x2, y2 = combination[1]
            opposite1 = (x2 + x2 - x1, y2 + y2 - y1)
            opposite2 = (x1 + x1 - x2, y1 + y1 - y2)
            if check_tuple_in_map(opposite1[0], opposite1[1], max_x, max_y, set_antinodes):
                set_antinodes.add(opposite1)
                count += 1
            if check_tuple_in_map(opposite2[0], opposite2[1], max_x, max_y, set_antinodes):
                set_antinodes.add(opposite2)
                count += 1
    return count


def check_tuple_in_map(x: int, y: int, max_x: int, max_y: int,
                       set_antinodes: set) -> bool:
    """
    Check tuple in map
    """
    if x < 0 or y < 0:
        return False
    if x >= max_x or y >= max_y:
        return False
    if (x, y) in set_antinodes:
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
