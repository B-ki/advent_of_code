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

class aoc_file:
    value: str
    index: int
    size: int
    used: bool = False

    def __init__(self, value: str, index: int, size: int):
        self.value = value
        self.index = index
        self.size = size

    def __str__(self):
        return f'[{self.value} {self.index} {self.size}]'


def get_list_aoc_file(data: list[str]) -> list[list[aoc_file]]:
    """
    Get the list of files from the data
    """
    dot_files: list[aoc_file] = []
    digit_files: list[aoc_file] = []
    all_files: list[aoc_file] = []
    i = 0
    while i < len(data):
        value = data[i]
        index = i
        size = 0
        while i < len(data) and data[i] == value:
            size += 1
            i += 1
        if value == '.':
            dot_files.append(aoc_file(value, index, size))
            all_files.append(aoc_file(value, index, size))
        else:
            digit_files.append(aoc_file(value, index, size))
            all_files.append(aoc_file(value, index, size))
    return [dot_files, digit_files, all_files]


def analyze_aoc_list(aoc_files: list[list[aoc_file]],
                     max_length: int) -> int:
    """
    Analyze the list of aoc files
    """
    digit_files = aoc_files[1]
    all_files = aoc_files[2]
    count = 0
    i = 0
    index = 0
    max_i = len(all_files)

    while index < max_length and i < max_i:
        curr_file = all_files[i]
        print(f'Index: {index}, i: {i}, File: {curr_file}')
        if curr_file.value != '.':
            for idx in range(index, index + curr_file.size):
                count += int(curr_file.value) * idx
                print(f'  Count += {int(curr_file.value)} * {idx} = {count}')
            index += curr_file.size
        else:
            size = curr_file.size
            fitting_index = find_fitting_files(digit_files, index, size)
            while fitting_index > 0:
                fitting_file = digit_files[fitting_index]
                for idx in range(index, index + fitting_file.size):
                    count += int(fitting_file.value) * idx
                    print(f'  Count += {int(fitting_file.value)} * {idx} = {count}')
                index += fitting_file.size
                size -= fitting_file.size
                digit_files[fitting_index].used = True
                if size == 0:
                    break
                print(f'Index: {index}, size: {size}')
                fitting_index = find_fitting_files(digit_files, index, size)
        i += 1

    return count


def analyze_v2(all_files: list[aoc_file]) -> list[aoc_file]:
    """
    Analyze the list of aoc files
    """
    max_i = len(all_files)
    i = max_i - 1
    while i > 0:
        curr_file = all_files[i]
        if curr_file.value != '.':
            space_index_in_list = find_fitting_space(all_files, curr_file)
            if space_index_in_list > 0:
                space_file = all_files[space_index_in_list]
                all_files[i].index = space_file.index
                all_files[space_index_in_list].size -= curr_file.size
                all_files[space_index_in_list].index += curr_file.size
        i -= 1

    return all_files


def checksum(all_files: list[aoc_file]) -> int:
    """
    Calculate the checksum
    """
    count = 0
    for file in all_files:
        if file.value != '.':
            for i in range(file.index, file.index + file.size):
                count += int(file.value) * i
    return count
       

def find_fitting_space(files: list[aoc_file], curr_file: aoc_file) -> int:
    """
    Find the fitting space for the current file
    """
    i = 0
    max_i = len(files)
    while files[i].index < curr_file.index and i < max_i:
        if files[i].value == '.' and files[i].size >= curr_file.size:
            return i
        i += 1
    return -1



def find_fitting_files(digit_files: list[aoc_file],
                       index: int, 
                       size: int) -> int:
    """
    Find the fitting files
    """
    i = len(digit_files) - 1
    while digit_files[i].index > index:
        print(f'find_fitting_loop: i: {i}, File: {digit_files[i]}, index: {index}')
        if digit_files[i].size <= size and not digit_files[i].used:
            print(f'    Fitting File: {digit_files[i]}')
            return i
        i -= 1
    return -1


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


def print_aoc_file_list(files: list[aoc_file]):
    """
    Print the list of aoc files
    """
    print("AOC Files: ")
    for file in files:
        print('    ', file)


def work(file_path: str) -> int:
    """
    Work on the given file path
    """
    data = get_input(file_path)
    new_data = create_disk_map(data)
    count = analyze_list(new_data)
    aoc_files = get_list_aoc_file(new_data)[2]
    print("Data: ", data)
    print("New Data: ", new_data)
    print("Count: ", count)
    count = checksum(analyze_v2(aoc_files))
    print(count)
    return count


def main():
    #work('example1.txt')
    work('example2.txt')
    #work('example3.txt')
    work('input.txt')

if __name__ == '__main__':
    main()
