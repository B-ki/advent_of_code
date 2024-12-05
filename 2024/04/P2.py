def get_input(file_path: str) -> list[str]:
    lines = []
    with open(file_path, 'r') as f:
        for line in f:
            lines.append(line.strip())
        return lines


def get_all_3x3_squares(lines: list[str]) -> int:
    """
    Get all 3x3 squares from the grid
    """
    count = 0
    max_x = len(lines[0])
    max_y = len(lines)
    for x in range(0, max_x - 2):
        for y in range(0, max_y - 2):
            if lines[y + 1][x + 1] != "A":
                continue
            first_diag = ""
            for k in range(3):
                first_diag += lines[y + k][x + k]
            second_diag = ""
            for k in range(3):
                second_diag += lines[y + 2 - k][x + k]
            if (
                    (first_diag == "MAS" or first_diag == "SAM") and 
                    (second_diag == "MAS" or second_diag == "SAM")
                ):
                count += 1
    return count


def main():
    print("Hello World!")
    example_lines = get_input("example.txt")
    print(example_lines)
    example_squares = get_all_3x3_squares(example_lines)
    print(example_squares)
    print(get_all_3x3_squares(get_input("input.txt")))


if __name__ == "__main__":
    main()
