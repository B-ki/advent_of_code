import numpy as np


def find_path(grid: np.array) -> int:
    """
    Find the number of paths from 0 to 9 in a grid
    :param grid: np.array
    :return: int
    """
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    memo = {}

    def dfs(x, y) -> int:
        """
        Depth First Search to find the number of paths from a start cell to the cell 9
        :param x: int
        :param y: int
        :return: int
        """
        # Pour chaque cellule, on compte le nombre de chemins possibles jusqu'à la cellule 9
        # On stocke le résultat dans un dictionnaire pour éviter de recalculer plusieurs
        if (x, y) in memo:
            return memo[(x, y)]

        if grid[x, y] == 9:
            return 1

        total_paths = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx, ny] == grid[x, y] + 1:
                # Récursion pour chaque cellule voisine
                total_paths += dfs(nx, ny)

        # On stock ici le nombre de chemins possibles pour chaque cellule
        memo[(x, y)] = total_paths
        return total_paths

    starts = np.argwhere(grid == 0)

    paths_count = np.zeros_like(grid, dtype=int)
    for x, y in starts:
        paths_count[x, y] = dfs(x, y)

    return np.sum(paths_count)


def get_input(file_path: str) -> np.array:
    """
    Transform into numpy array a text input like :
    0123
    1234
    8765
    9876
    """
    with open(file_path, 'r') as f:
        return np.array([[int(i) for i in line.strip()] for line in f.readlines()])


def work(file_path: str) -> None:
    """
    Print the number of paths from 0 to 9 in a grid
    :param file_path: str
    """
    input_data = get_input(file_path)
    print(input_data)
    print(find_path(input_data))


def main():
    work('example.txt')
    work('input.txt')


if __name__ == '__main__':
    main()
