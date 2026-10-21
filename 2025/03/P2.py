def loop_over_input(list_input: list[str]) -> int:
    count = 0
    for line in list_input:
        count += get_highest_jolltage(line)
    return count


def get_highest_jolltage(bank: str) -> int:
    list_int = [int(c) for c in bank]
    bank_list = []
    for i in range(1, 13):
        restricted_list = list_int
        if i != 12:
            restricted_list = list_int[:-(12-i)]
        max_int = max(restricted_list)
        index = restricted_list.index(max_int)
        list_int = list_int[index+1:]
        bank_list.append(max_int)
        #print(f"i = {i}, restricted_list = {restricted_list}, max_int = {max_int}, index = {index}, l = {list_int}")
    return int("".join(map(str, bank_list)))


def get_list_input(path: str) -> list[str]:
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]


def main():
    print(loop_over_input(get_list_input("input_test.txt")))
    print(loop_over_input(get_list_input("input.txt")))
    assert ((get_highest_jolltage("987654321111111")
        + get_highest_jolltage("811111111111119")
        + get_highest_jolltage("234234234234278")
        + get_highest_jolltage("818181911112111"))
        == 3121910778619)


if __name__ == "__main__":
    main()
