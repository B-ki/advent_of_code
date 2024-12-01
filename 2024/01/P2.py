def get_lists_from_file(file_path: str) -> list(list()):
    """
    Read the file and return the two lists
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    list_1: list(int) = []
    list_2: list(int) = []
    for line in lines:
        list_1.append(int(line.split()[0]))
        list_2.append(int(line.split()[1]))
    list_1.sort()
    list_2.sort()
    return [list_1, list_2]


def calculate_difference(list_1: list, list_2: list) -> int:
    """
    Calculate the difference between the two lists
    """
    distances = 0
    for i, j in zip(list_1, list_2):
        if i > j:
            distances += i - j
        else:
            distances += j - i
    return distances


def count_appearances(list_1: list, list_2: list) -> int:
    """
    Count the number of times the two lists have the same number
    """
    total = 0
    for i in list_1:
        total += i * list_2.count(i)
    return total

def get_result_from_file(file_path: str) -> int:
    """
    Get the result from the file
    """
    two_list = get_lists_from_file(file_path)
    list_1 = two_list[0]
    list_2 = two_list[1]
    return count_appearances(list_1, list_2)


def main():
    print("Hello, World!")
    print(get_result_from_file("example.txt"))
    print(get_result_from_file("input.txt"))


if __name__ == "__main__":
    main()
