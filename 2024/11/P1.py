
def blink_n_times(stones: list[str], n: int) -> list[str]:
    """
    Blink the stones n times
    """
    for _ in range(n):
        stones = blink(stones)
        #print(f'After blinking {n} times:\n{stones}')
    return stones


def blink(stones: list[str]) -> list[str]:
    """
    Blink the stones
    """
    new_stones: list[str] = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        else:
            if len(stone) % 2 == 0:
                length = len(stone)
                #print(f'stone: {stone}')
                #print(f'first half: {stone[0: length // 2]}')
                #print(f'second half: {stone[length // 2:length]}')
                new_stones.append(str(int(stone[0: length // 2])))
                new_stones.append(str(int(stone[length // 2:length])))
            else:
                new_stones.append(str(int(stone) * 2024))
    return new_stones


def get_input(file_path: str) -> list[str]:
    """
    Transform an input like : 4022724 951333 0 21633 5857 97 702 6
    into a list of strings
    """
    with open(file_path, 'r') as file:
        return file.read().split()


def work(file_path: str) -> int:
    """
    Work function
    """
    data = get_input(file_path)
    print(data)
    data = blink_n_times(data, 25)
    print(f'After blinking 25 times, we have {len(data)} stones')
    return len(data)


def main() -> None:
    """
    Main function
    """
    work("example2.txt")
    print("\n")
    work("input.txt")


if __name__ == "__main__":
    main()
