import re


def reverse(list_line: list[str]) -> list[str]:
    """
    Create reverse input
    """
    reverse_lines = []
    for line in list_line:
        reverse_lines.append(line[::-1])
    return reverse_lines


def get_diagonal_lines(list_line: list[str]) -> list[str]:
    """
    Create diagonal input
    """
    max_x = len(list_line[0])
    max_y = len(list_line)
    minimum = min(max_x, max_y)
    all_diagonal = []
    for x in range(1, max_x):
        diagonal = ""
        y = 0
        i = x
        j = y
        while (i >= 0 and i < max_x and j >= 0 and j < max_y):
            diagonal += list_line[j][i]
            i += 1
            j += 1
        all_diagonal.append(diagonal)
    for y in range(1, max_y):
        diagonal = ""
        x = 0
        i = x
        j = y
        while (i >= 0 and i < max_x and j >= 0 and j < max_y):
            diagonal += list_line[j][i]
            i += 1
            j += 1
        all_diagonal.append(diagonal)
    diagonal = ""
    for i, j in zip(range(0, minimum), range(0, minimum)):
        diagonal += list_line[i][j]
    all_diagonal.append(diagonal)
    return all_diagonal


def get_other_diagonal_lines(list_line: list[str]) -> list[str]:
    all_diagonal = []
    max_x = len(list_line[0])
    max_y = len(list_line)
    for x in range(1, max_x):
        diagonal = ""
        y = max_y - 1
        i = x
        j = y
        while (i >= 0 and i < max_x and j >= 0 and j < max_y):
            diagonal += list_line[j][i]
            i += 1
            j -= 1
        all_diagonal.append(diagonal)
    for y in range(0, max_y - 1):
        diagonal = ""
        x = 0
        i = x
        j = y
        while (i >= 0 and i < max_x and j >= 0 and j < max_y):
            diagonal += list_line[j][i]
            i += 1
            j -= 1
        all_diagonal.append(diagonal)
    diagonal = ""
    for i, j in zip(range(0, max_x), range(max_y - 1, -1, -1)):
        diagonal += list_line[j][i]
    all_diagonal.append(diagonal)
    return all_diagonal


def get_vertical_lines(horizontal_lines: list[str]) -> list[str]:
    """
    Get vertical lines
    """
    vertical_lines = []
    max_x = len(horizontal_lines[0])
    max_y = len(horizontal_lines)
    print("max_x: ", max_x)
    print("max_y: ", max_y)
    for x in range(0, max_x):
        vertical = ""
        for y in range(0, max_y):
            vertical += horizontal_lines[y][x]
        vertical_lines.append(vertical)
    return vertical_lines


def get_horizontal_lines(file_path: str) -> list[str]:
    """
    Get all lines in file
    """
    horizontal_lines = []
    with open(file_path, "r") as file:
        for line in file:
            horizontal_lines.append(line.strip())
        return horizontal_lines


def get_all_lines(file_path: str) -> list[str]:
    """
    Get all lines in file
    """
    horizontal_lines = get_horizontal_lines(file_path)
    reverse_horizontal = reverse(horizontal_lines)
    vertical_lines = get_vertical_lines(horizontal_lines)
    reverse_vertical = reverse(vertical_lines)
    diagonal_1 = get_diagonal_lines(horizontal_lines)
    reverse_diagonal_1 = reverse(diagonal_1)
    diagonal_2 = get_other_diagonal_lines(horizontal_lines)
    reverse_diagonal_2 = reverse(diagonal_2)
    return horizontal_lines + reverse_horizontal + vertical_lines + reverse_vertical + diagonal_1 + reverse_diagonal_1 + diagonal_2 + reverse_diagonal_2


def count_XMAS(list_line: list[str]) -> int:
    """
    Search for XMAS pattern in strings. Can have multiple pattern in one string
    Need flag gm to search for multiple pattern in one string
    """
    pattern = r"XMAS"
    count = 0
    for line in list_line:
        if len(re.findall(pattern, line)) == 0:
            print(line)
        count += len(re.findall(pattern, line))
    return count


def main():
    print("Hello, World!")
    print(len("0123456789"))
    print("range(0, 10): ", list(range(0, 10)))
    print("range(0, 1): ", list(range(0, 1)))
    print("range(10, -1, -1): ", list(range(10, -1, -1)))
    all_lines = get_all_lines("example.txt")
    #print(all_lines)
    print(count_XMAS(all_lines))
    input_lines = get_all_lines("input.txt")
    print(count_XMAS(input_lines))


if __name__ == "__main__":
    main()
