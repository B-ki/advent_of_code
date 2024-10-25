import numpy as np


class LagrangePoly:

    def __init__(self, X, Y):
        self.n = len(X)
        self.X = np.array(X)
        self.Y = np.array(Y)

    def li(self, x, i):
        return np.prod([(x - self.X[j]) / (self.X[i] - self.X[j])
                        for j in range(self.n) if j != i])

    def Li(self, x):
        return np.sum([self.Y[i] * self.li(x, i) for i in range(self.n)])

    def __call__(self, x):
        return self.Li(x)


def read_input(file_path: str) -> list[list[int]]:
    """
    read the input file and return a reverse list of list of integers
    """
    list_of_list = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line_list = list(map(int, line.strip().split()))
            line_list.reverse()
            list_of_list.append(line_list)
    return list_of_list


def get_abscissa(list_int: list[int]) -> list[int]:
    """
    return [0, 1, ..., n] with n = len(list_int)
    """
    return list(range(len(list_int)))


def find_next_value(ordinates: list[int]) -> int:
    """
    find the next value of the Lagrange polynomial
    """
    f = LagrangePoly(get_abscissa(ordinates), ordinates)
    return f(len(ordinates))


def calculate(file_path: str) -> int:
    """
    calculate the sum of the next values of the Lagrange polynomial
    """
    data = read_input(file_path)
    sum_next_values = 0
    for ordinates in data:
        #print(ordinates, find_next_value(ordinates))
        sum_next_values += find_next_value(ordinates)
    return sum_next_values


def main():
    X = [0, 1, 2, 3, 4]
    Y = [3, 6, 9, 12, 15]
    f = LagrangePoly(X, Y)
    print(f(5))
    print(find_next_value(Y))
    print(calculate('input_test.txt'))
    print(calculate('input_1.txt'))


if __name__ == '__main__':
    main()
