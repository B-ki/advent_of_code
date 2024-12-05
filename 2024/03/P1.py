import re


def parse_multiple_pattern(text: str) -> int:
    """
    Find pattern like :
    - mul(A,B) with A and B int 1 to 3 digits
    """
    pattern = r"mul\((\-?\d{1,3})\,(\-?\d{1,3})\)"
    matches = re.findall(pattern, text)
    return sum([int(a) * int(b) for a, b in matches])


def get_input(file_path: str) -> str:
    """
    Get input as string
    """
    with open(file_path, "r") as file:
        return file.read().replace("\n", "")


def test() -> None:
    """
    Test example given in subject
    """
    assert parse_multiple_pattern(get_input("example.txt")) == 161
    print("Test 1 : example == 161")


def main():
    test()
    print("Hello, World!")
    print(get_input("example.txt"))
    print(parse_multiple_pattern(get_input("example.txt")))
    print(parse_multiple_pattern(get_input("input.txt")))


if __name__ == "__main__":
    main()
