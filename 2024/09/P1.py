def get_list_non_empty_index(data: list[str]) -> list[int]:
    """
    Get the index of all the non-dot values in the data
    """
    non_empty_index: list[int] = []
    for i in range(len(data)):
        if data[i] != '.':
            non_empty_index.append(i)
    return non_empty_index


def get_list_dot_index(data: list[str]) -> list[int]:
    """
    Get the index of all the dots in the data
    """
    dot_index: list[int] = []
    for i in range(len(data)):
        if data[i] == '.':
            dot_index.append(i)
    return dot_index


def analyze_list(data: list[str]) -> int:
    """
    Optimized algorithm to count diskmap value
    """
    digit_index: list[int] = get_list_non_empty_index(data)
    dot_index: list[int] = get_list_dot_index(data)
    max_index: int = len(digit_index)
    count: int = 0
    i: int = 0
    while digit_index[i] < max_index:
        count += digit_index[i] * int(data[digit_index[i]])
        i += 1
    i = 0
    j: int = max_index - 1
    while dot_index[i] < max_index:
        count += dot_index[i] * int(data[digit_index[j]])
        i += 1
        j -= 1
    return count


def create_disk_map(data: str) -> list[str]:
    """
    Create a new disk map from the given data
    """
    new_data = []
    ID = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for _ in range(int(data[i])): 
                new_data.append(str(ID))
            ID += 1
        else:
            new_data += '.' * int(data[i])
    return new_data


def get_input(file_path: str) -> str:
    """
    Get the input data from the file
    """
    with open(file_path, 'r') as f:
        return f.read().strip()


def main():
    example_data = get_input('example3.txt')
    example2_data = get_input('example2.txt')
    print(example_data)
    print(example2_data)
    new_data_example1 = create_disk_map(example_data)
    new_data_example2 = create_disk_map(example2_data)
    print(new_data_example1)
    print(new_data_example2)
    print(analyze_list(new_data_example1))
    print(analyze_list(new_data_example2))
    input_data = get_input('input.txt')
    new_data = create_disk_map(input_data)
    final_count = analyze_list(new_data)
    print(final_count)


if __name__ == '__main__':
    main()
