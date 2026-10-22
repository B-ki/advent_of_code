def get_input(path: str) -> list[str]:
    grid: list[str] = []
    with open(path, "r") as f:
        for line in f:
            grid.append(line.strip())
    return grid


def check_accessible_paper_roll(grid: list[str], i: int, j: int) -> bool:
    up = max(0, j - 1)
    down = min(len(grid) - 1, j + 1)
    right = min(len(grid[0]) - 1, i + 1)
    left = max(0, i - 1)
    count = 0
    #print(f"Checking accessible paper roll at ({i}, {j})")
    #print(f"Bounds: left={left}, right={right}, up={up}, down={down}")
    for x in range(left, right + 1):
        for y in range(up, down + 1):
            #print(f"x, y: {x}, {y}, count = {count}")
            if grid[y][x] == "@" and (x != i or y != j):
                count += 1
                if count >= 4:
                    return False
    return True


def count_accessible_paper_roll(grid: list[str]) -> int:
    count = 0
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == "@":
                if check_accessible_paper_roll(grid, i, j):
                    count += 1
    return count


def main():
    print("Hello, World!")
    grid = get_input("input.txt")
    print(count_accessible_paper_roll(grid))


if __name__ == "__main__":
    main()
