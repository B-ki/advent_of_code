from typing import List 
from typing import Tuple


def read_input(file_path: str) -> List[Tuple[int, int]]:
    '''Create a matrix from a file.'''
    matrix: List[Tuple[int, int]] = []
    times: List[int] = []
    distance: List[int] = []

    with open(file_path, 'r') as file:
        for line in file:
            if line[0] == 'T':
                times = list(map(int, line.split()[1:]))
            elif line[0] == 'D':
                distance = list(map(int, line.split()[1:]))

    matrix = list(zip(times, distance))

    return matrix

def get_number_win(tup: Tuple[int, int]) -> int:
    '''Estimate how many winable solution there is'''
    tot_sol: int = 0
    for s in range(0, tup[0]):
        if s * (tup[0] - s) > tup[1]:
            tot_sol += 1
    return tot_sol


def main():
    matrix: List[Tuple[int, int]] = read_input("inputP1.txt")
    print(matrix)
    list_nb_sol: List[int] = []
    for tup in matrix:
        list_nb_sol.append(get_number_win(tup))
    res: int = 1
    for e in list_nb_sol:
        res *= e
    print(res)


if __name__ == '__main__':
    main()
