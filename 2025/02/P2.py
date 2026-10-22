RANGES: list[tuple[int, int]] = [
    (11, 22),
    (95, 115),
    (998, 1012),
    (1188511880, 1188511890),
    (222220, 222224),
    (1698522, 1698528),
    (446443, 446449),
    (38593856, 38593862),
    (565653, 565659),
    (824824821, 824824827),
    (2121212118, 2121212124),
]

def is_invalid_id(string_id: str) -> int:
    """
    If a string is made of 2 sequences repeated twice in the string, it is 
    invalid.
    Ex : 55 is invalid, 6464 too, but 191918 isn't
    """
    count = 0
    length = len(string_id)
    half_length = int(length/2)
    for start in range(1, half_length + 1):
        s = string_id[0:start]
        #print(string_id, half_length, s, s*int(length/start), string_id == s*int(length/start))
        if string_id == s*int(length/start):
            count += int(string_id)
            break
    return count


def loop_over_input(tuple_list: list[tuple]) -> int:
    count = 0
    for tup in tuple_list:
        for i in range(tup[0], tup[1]+1):
            count += is_invalid_id(str(i))
    return count


def get_input(path: str) -> list:
    with open(path, 'r') as file:
        lines = file.readlines()
    tuple_list: list[tuple] = []
    for id_range in lines[0].split(','):
        start, end = map(int, id_range.split('-'))
        tuple_list.append((start, end))
    return tuple_list


def main():
    print(loop_over_input(RANGES))
    print(loop_over_input(get_input('input.txt')))



if __name__ == "__main__":
    main()
