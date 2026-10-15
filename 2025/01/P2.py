def check_if_0_reached(position: int, move_tuple: tuple) -> int:
    direction, steps = move_tuple
    if direction == 'L':
        position = (100 - position) % 100
    #if direction == 'R':
    #    position = (100 + position) % 100
    return (position + steps) // 100


def loop_over_input(tuple_list: list[tuple]) -> int:
    count = 0
    position = 50
    for tup in tuple_list:
        print(tup, position)
        count += check_if_0_reached(position, tup)
        position = move_dial(position, tup)
        print("count :", count)
    return count


def move_dial(start_position: int, move_tuple: tuple) -> int:
    if move_tuple[0] == 'L':
        return (start_position - move_tuple[1]) % 100
    elif move_tuple[0] == 'R':
        return (start_position + move_tuple[1]) % 100
    else:
        return -1


def get_input_list(path: str) -> list[tuple]:
    with open(path, 'r') as file:
        lines = file.readlines()
    tuple_list: list[tuple] = []
    for line in lines:
       tuple_list.append((line[0], int(line[1:])))
    return tuple_list


def main():
    print(loop_over_input(get_input_list('input_p1.txt')))


if __name__ == "__main__":
    main()
