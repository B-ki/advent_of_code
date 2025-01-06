import numpy as np
from collections import deque


def find_path(grid: np.array) -> int:
    """
    Find if the number of summits reachable by each 0 cell in the grid
    :param grid: np.array
    :return: int
    """
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start) -> int:
        """
        Breadth First Search to find the number of summits reachable from a start cell
        :param start: tuple
        :return: int
        """
        queue = deque([start])
        visited = np.zeros_like(grid, dtype=bool)
        visited[start] = True
        
        summit_count = 0
        while queue:
            x, y = queue.popleft()
            
            if grid[x, y] == 9:
                summit_count += 1
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx, ny]:
                    if grid[nx, ny] - grid[x, y] == 1:
                        visited[nx, ny] = True
                        queue.append((nx, ny))
        
        return summit_count
    
    starts = np.argwhere(grid == 0)
    
    all_count = 0
    for start in starts:
        count = bfs(tuple(start))
        all_count += count 
    return all_count


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
    input_data = get_input(file_path)
    print(input_data)
    print(find_path(input_data))


def main():
    work('example.txt')
    work('input.txt')


if __name__ == '__main__':
    main()
