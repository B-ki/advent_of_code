import re


def parse_multiple_pattern(text: str) -> list:
    """
    Find pattern like :
    - mul(A,B) with A and B int 1 to 3 digits
    - do()
    - don't()
    """
    pattern = r"mul\((\-?\d{1,3})\,(\-?\d{1,3})\)|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        if match[0] and match[1]:
            result.append(int(match[0]) * int(match[1]))
        else:
            if match[2]:
                result.append("do")
            else:
                result.append("dont")
    return result


def treat_result(parsed_list: list) -> int:
    """
    Add numbers in list, unless a dont is found
    If a dont is found, skip to the next do
    Then start again
    """
    i = 0
    total = 0
    len_list = len(parsed_list)
    while i < len_list:
        if parsed_list[i] == "do":
            i += 1
        elif parsed_list[i] == "dont":
            while i < len_list and parsed_list[i] != "do":
                i += 1
        else:
            total += int(parsed_list[i])
            i += 1
    return total


def get_input(file_path: str) -> str:
    """
    Get input as text
    """
    with open(file_path, "r") as file:
        return file.read().replace("\n", "")


def main():
    example_list = parse_multiple_pattern(get_input("example2.txt"))
    result_example = treat_result(example_list)
    assert result_example == 48
    input_list = parse_multiple_pattern(get_input("input.txt"))
    result = treat_result(input_list)
    print(result)


if __name__ == "__main__":
    main()
