from typing import Tuple


def read_input(file_path: str) -> Tuple[int, int]:
    '''Create a matrix from a file.'''
    time_string: str = ""
    dist_string: str = ""

    with open(file_path, 'r') as file:
        for line in file:
            if line[0] == 'T':
                for char in line:
                    if char.isdigit():
                        time_string += char
            elif line[0] == 'D':
                for char in line:
                    if char.isdigit():
                        dist_string += char
    return (int(time_string), int(dist_string))

def get_number_win(tup: Tuple[int, int]) -> int:
    '''Estimate how many winable solution there is'''
    tot_sol: int = 0
    for s in range(0, tup[0]):
        if s * (tup[0] - s) > tup[1]:
            tot_sol += 1
    return tot_sol


def main():
    tuple: Tuple[int, int]= read_input("inputP1.txt")
    print(tuple)
    print(get_number_win(tuple))


if __name__ == '__main__':
    main()
