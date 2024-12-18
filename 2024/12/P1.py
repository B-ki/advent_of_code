import numpy as np
from collections import deque

def get_score(grid: np.array) -> None:
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = np.zeros_like(grid, dtype=bool)
    new_grid = np.empty(grid.shape, dtype=object)
    dict_letter: dict[str, int] = {}

    def bfs_area(sx, sy, letter, new_letter) -> None:
        queue = deque([(sx, sy)])
        while queue:
            x, y = queue.popleft()
            visited[x, y] = True
            new_grid[x, y] = new_letter
            print(f"new_grid[{x}, {y}] = {new_letter}")
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                        0 <= nx < rows and 0 <= ny < cols 
                        and not visited[(x, y)]
                        and grid[nx, ny] == letter
                    ):
                    visited[(nx, ny)] = True
                    queue.append((nx, ny))

    print(new_grid)

    for x in range(rows):
        for y in range(cols):
            if not visited[x, y]:
                letter = grid[x, y]
                if letter in dict_letter:
                    dict_letter[letter] += 1
                    new_str = letter + str(dict_letter[letter])
                else:
                    dict_letter[letter] = 0
                    new_str = letter + "0"

                print(f"New letter: {new_str}, x: {x}, y: {y}")
                bfs_area(x, y, grid[x, y], new_str)

    print(new_grid)
                    


def get_input(file_path: str) -> np.array:
    """
    Transform into np array an input like : 
    RRRRIICCFF
    MIIISIJEEE
    MMMISSJEEE
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return np.array([list(line.strip()) for line in lines])


def work(file_path: str) -> None:
    data = get_input(file_path)
    print(data)
    get_score(data)



def main():
    work('example.txt')
    #work('input.txt')


if __name__ == '__main__':
    main()
