def loop_over_input(list_input: list[str]) -> int:
    count = 0
    for line in list_input:
        count += get_highest_battery(line)
    return count


def get_highest_battery(bank: str) -> int:
    list_int = [int(c) for c in bank]
    x = list_int[0]
    y = list_int[1]
    m = len(list_int)
    for i in range(2, m):
        #print(f"i: {i}, x: {x}, y: {y}, list_int[i]: {list_int[i]}, m: {m}")
        if list_int[i] > x and i < m - 1:
            x = list_int[i]
            y = 0
        else:
            if list_int[i] >= y:
                y = list_int[i]
    return x * 10 + y


def get_list_input(path: str) -> list[str]:
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]


def main():
    print(loop_over_input(get_list_input("input_test.txt")))
    print(loop_over_input(get_list_input("input.txt")))


if __name__ == "__main__":
    main()
