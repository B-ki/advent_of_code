def loop_over_input(id_range_list: list[tuple[int, int]],
                    id_list: list[int]) -> int:
    """
    Loop over the input
    """
    count: int = 0
    ranges = sorted(id_range_list)
    cur_a, cur_b = ranges[0]
    count += cur_b - cur_a + 1
    for a, b in ranges[1:]:
        if a <= cur_b:
            if b > cur_b:
                count += b - cur_b
                cur_b = b
        else:
            count += b - a + 1
            cur_a, cur_b = a, b
    return count

def get_input(path: str) -> tuple[list[tuple[int, int]], list[int]]:
    """
    From input return :
    - list of id range ([3, 5], [10-14], etc.)
    - list of id (1, 2, 3, 4, etc.)
    """
    id_range_list: list[tuple[int, int]] = []
    id_list: list[int] = []
    with open(path, "r") as f:
        id_range_txt, id_txt = f.read().split("\n\n")
        for l in id_range_txt.splitlines():
            a, b = l.split("-")
            id_range_list.append((int(a), int(b)))
        for l in id_txt.splitlines():
            id_list.append(int(l))
    return id_range_list, id_list


def main():
    print("Hello World!")
    id_range_list, id_list = get_input("input.txt")
    print(loop_over_input(id_range_list, id_list))


if __name__ == "__main__":
    main()
