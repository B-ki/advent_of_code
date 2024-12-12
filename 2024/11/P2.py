import math


def blink_n_times(stones: list[int], n: int) -> list[int]:
    """
    Blink the stones n times
    """
    memo: dict[int, list[int]] = {0: [1]}

    def blink(stones: list[int]) -> list[int]:
        """
        Blink the stones
        """
        new_stones: list[int] = []
        for stone in stones:
            if stone in memo:
                for s in memo[stone]:
                    new_stones.append(s)
                continue
            elif stone == 0:
                new_stones.append(1)
            else:
                length = int(math.log10(int(stone))) + 1
                if length % 2 == 0:
                    new_stones.append(int(stone / (10 ** (length // 2))))
                    new_stones.append(int(stone % (10 ** (length // 2))))
                    memo[stone] = [int(stone / (10 ** (length // 2))),
                                   int(stone % (10 ** (length // 2)))]
                else:
                    new_stones.append(stone * 2024)
                    memo[stone] = [stone * 2024]
        return new_stones

    for _ in range(n):
        stones = blink(stones)
    return stones




def get_input(file_path: str) -> list[int]:
    """
    Transform an input like : 4022724 951333 0 21633 5857 97 702 6
    into a list of strings
    """
    with open(file_path, 'r') as file:
        return [int(x) for x in file.readline().split()]


def work(file_path: str) -> int:
    """
    Work function
    """
    data = get_input(file_path)
    print(data)
    count = 0
    for stone in data:
        new_stones = blink_n_times([stone], 50)
        count += len(new_stones)
    print(f'After blinking 75 times, we have {count} stones')
    return len(data)


def main() -> None:
    """
    Main function
    """
    work("example2.txt")
    print("\n")
    #work("input.txt")


if __name__ == "__main__":
    main()
