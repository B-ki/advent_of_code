RESTART_WITHOUT_FIRST_ELEMENT = True

def get_lists_from_file(file_path: str) -> list(list()):
    """
    Read the file and return the two lists
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    all_list = []
    for line in lines:
        all_list.append([int(number) for number in line.split()])
    return all_list


def respect_order(order: int, previous_number: int, number: int) -> bool:
    """
    """
    if order == 1:
        if previous_number > number and previous_number <= 3 + number:
            return True
        else:
            return False
    else:
        if previous_number < number and number <= previous_number + 3:
            return True
        else:
            return False


def get_list_order(actual_list: list()) -> int:
    sum_difference = 0
    for i in range(len(actual_list) - 1):
        if i < len(actual_list) - 1:
            sum_difference += actual_list[i] - actual_list[i + 1]
    if sum_difference == 0:
        return 0
    sum_difference = sum_difference / abs(sum_difference)
    print("list:", actual_list, "sum_difference:", sum_difference)
    return sum_difference


def test_list_safety(actual_list: list(), restarted: bool) -> int:
    previous_number = actual_list[0]
    order = get_list_order(actual_list)
    if order == 0:
        print(actual_list)
        return 0
    last_index = len(actual_list) - 1
    dampener = 1
    for i, number in enumerate(actual_list[1:]):
        if order == 1:
            if respect_order(order, previous_number, number):
                if i + 1 == last_index:
                    return 1
                previous_number = number
                continue
            else:
                if dampener == 1:
                    if i + 1 == last_index:
                        return 1
                    dampener = 0
                    continue
                else:
                    if restarted == False and i == 2:
                        return test_list_safety(actual_list[1:], True)
                    return 0
        else:
            if respect_order(order, previous_number, number):
                if i + 1 == last_index:
                    return 1
                previous_number = number
                continue
            else:
                if dampener == 1:
                    if i + 1 == last_index:
                        return 1
                    dampener = 0
                    continue
                else:
                    if restarted == False and i == 2:
                        return test_list_safety(actual_list[1:], True)
                    return 0


def calculate_list(all_list: list(list())) -> int:
    """
    """
    total_safe = 0
    for actual_list in all_list:
        total_safe += test_list_safety(actual_list, False)
    return total_safe


def main():
    print("Hello, World!")
    print(calculate_list(get_lists_from_file("example.txt")))
    print(calculate_list(get_lists_from_file("input.txt")))
    

if __name__ == "__main__":
    main()
