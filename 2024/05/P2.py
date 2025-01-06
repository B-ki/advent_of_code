
def get_input(file_path: str) -> list[list[list[int]]]:
    p1_input = []
    p2_input = []
    change = False
    with open(file_path, "r") as file:
        for line in file:
            if change == False:
                if line == "\n":
                    change = True
                    continue
                else:
                    p1_input.append([int(n) for n in line.strip().split("|")])
            else:
                p2_input.append([int(n) for n in line.strip().split(",")])
    return [p1_input, p2_input]


def create_dict_before(p1: list[list[int]]) -> dict[int, list[int]]:
    dict_before: dict[int, list[int]] = {}
    for line in p1:
        if line[0]  not in dict_before:
            dict_before[line[0]] = [line[1]]
        else:
            dict_before[line[0]].append(line[1])
    return dict_before


def create_dict_after(p1: list[list[int]]) -> dict[int, list[int]]:
    dict_after: dict[int, list[int]] = {}
    for line in p1:
        if line[1]  not in dict_after:
            dict_after[line[1]] = [line[0]]
        else:
            dict_after[line[1]].append(line[0])
    return dict_after


def check_instruction(instruction: list[int],
                      dict_before: dict[int, list[int]],
                      dict_after: dict[int, list[int]]) -> bool:
    for i in range(1, len(instruction)):
        for j in range(0, i):
            if (
                    instruction[i] in dict_before
                    and instruction[j] in dict_before[instruction[i]]
                ): 
                return False
        for j in range(i+1, len(instruction)):
            if (
                    instruction[i] in dict_after
                    and instruction[j] in dict_after[instruction[i]]
                ): 
                return False
    return True


def check_all_instructions(p2: list[list[int]],
                           dict_before: dict[int, list[int]],
                           dict_after: dict[int, list[int]]) -> int:
    count = 0
    for instruction in p2:
        if check_instruction(instruction, dict_before, dict_after) == False:
            instruction = correct_instruction(instruction, dict_before, dict_after)
            count += instruction[int(len(instruction)/2)]
    return count


def find_first_error(instruction: list[int],
                             dict_before: dict[int, list[int]],
                             dict_after: dict[int, list[int]]) -> tuple[int, int]:
    for i in range(1, len(instruction)):
        for j in range(0, i):
            if (
                    instruction[i] in dict_before
                    and instruction[j] in dict_before[instruction[i]]
                ): 
                return -i, -j
        for j in range(i+1, len(instruction)):
            if (
                    instruction[i] in dict_after
                    and instruction[j] in dict_after[instruction[i]]
                ): 
                return i, j
    return 0, 0


def correct_instruction(instruction: list[int],
                        dict_before: dict[int, list[int]],
                        dict_after: dict[int, list[int]]) -> list[int]:
    i, j = find_first_error(instruction, dict_before, dict_after)
    #print(instruction, "error:", i, j)
    while i != 0:
        if i < 0:
            tmp = instruction[-i]
            instruction[-i] = instruction[-j]
            instruction[-j] = tmp
        else:
            tmp = instruction[i]
            instruction[i] = instruction[j]
            instruction[j] = tmp
        i, j = find_first_error(instruction, dict_before, dict_after)
        #print(instruction, "error:", i, j)
    return instruction


def main():
    print("Hello, World!")
    p1 = get_input("input.txt")[0]
    p2 = get_input("input.txt")[1]
    print(p1)
    print(p2)
    dict_before = create_dict_before(p1)
    dict_after = create_dict_after(p1)
    print(dict_before)
    print(dict_after)
    print(check_all_instructions(p2, dict_before, dict_after))


if __name__ == "__main__":
    main()
