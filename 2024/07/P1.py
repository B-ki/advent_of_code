def can_create_value(value: int, nb: list[int]) -> bool:
    memo = {}

    def backtrack(remaining: list[int]) -> bool:
        state = (tuple(sorted(remaining)))
        if state in memo:
            return memo[state]

        if len(remaining) == 1:
            if remaining[0] == value:
                return True
            else:
                return False
        if multiply_all(remaining) < value:
            return False
        if sum(remaining) > value:
            return False
        if max(remaining) > value:
            return False

        for i in range(len(remaining)):
            for j in range(i + 1, len(remaining)):
                a, b = remaining[i], remaining[j]
                next_numbers = [remaining[k] for k in range(len(remaining)) if k != i and k != j]
                if backtrack(next_numbers + [a + b]):
                    memo[state] = True
                    return True
                if backtrack(next_numbers + [a * b]):
                    memo[state] = True
                    return True
        memo[state] = False
        return False

    return backtrack(sorted(nb, reverse=True))


def multiply_all(nb: list[int]) -> int:
    result = 1
    for i in nb:
        result *= i
    return result


def count_correct_equation(file_path: str) -> int:
    all_line_list = get_input(file_path)
    count = 0
    for line in all_line_list:
        print(line)
        if multiply_all(line[1]) < line[0]:
            continue
        if can_create_value(line[0], line[1]):
            count += line[0]
    return count


def get_input(file_path: str) -> list[list[int]]:
    all_line_list = []
    with open(file_path, 'r') as f:
        for line in f:
            line_list = []
            line_list.append(int(line.split(":")[0]))
            line_list.append([int(x) for x in line.split(":")[1].split()])
            all_line_list.append(line_list)
    return all_line_list


def main():
    file_path = "input.txt"
    print(get_input(file_path))
    print(count_correct_equation(file_path))


if __name__ == "__main__":
    main()
