def get_input(file_path: str) -> str:
    """
    Open a text file and get the content of the file
    """
    with open(file_path, "r") as file:
        return file.read()


def treat_input(input_str: str) -> tuple[str, list]:
    """
    Treat the input string and return :
    - first line = directions 'RRRLLRLRLR...'
    - all lines starting 3d line = map 'AAA = (BBB, CCC)', ...
    """
    lines = input_str.split("\n")
    return (lines[0], lines[2:])


def create_adjacency_list(map_list: list[str]) -> dict:
    """
    Create an adjacency list from the map
    """
    adjacency_list = {}
    for line in map_list:
        if line == "":
            break
        node, branches = line.split(" = ")
        branches = tuple(branches.strip(" ()").split(", "))
        adjacency_list[node] = branches
    return adjacency_list


def browse_dict_map(dict_map: dict, directions:str, node: str) -> int:
    """
    Browse the adjacency list according to the directions
    """
    i = 0
    while node[2] != "Z":
        for direction in directions:
            if node[2] == "Z":
                return i
            if direction == "L":
                direction_int = 0
            else:
                direction_int = 1
            node = dict_map[node][direction_int]
            i+=1
    return i


def get_starting_nodes(dict_map: dict) -> list:
    """
    Get the starting nodes of the map, which ends with "A"
    """
    starting_nodes = []
    for key in dict_map.keys():
        if key[2] == "A":
            starting_nodes.append(key)
    return starting_nodes


def check_if_all_nodes_are_end(list_nodes: list) -> bool:
    """
    Check if all nodes are end nodes, which ends with "Z"
    """
    for node in list_nodes:
        if node[2] != "Z":
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor
    """
    temp = min(a, b)
    while a != b and b > 0:
        temp = min(a, b)
        a = max(a, b)
        a = a - temp
        b = temp
    return a


def lcm(a: int, b: int) -> int:
    """
    Calculate the least common multiple
    """
    return a * b // gcd(a, b)


def count_steps(file_path: str) -> int:
    """
    Count the number of steps to reach the end
    """
    input_lines = get_input(file_path)
    directions, map_list = treat_input(input_lines) 
    dict_map = create_adjacency_list(map_list)
    starting_nodes = get_starting_nodes(dict_map)
    list_iterations_first_Z: list[int] = []
    for node in starting_nodes:
        list_iterations_first_Z.append(browse_dict_map(dict_map, directions, node))
    lcm_value = 1
    for iteration in list_iterations_first_Z:
        lcm_value = lcm(lcm_value, iteration)
    print(list_iterations_first_Z)
    return lcm_value


def main():
    print(gcd(12, 15))
    assert(gcd(12, 15) == 3)
    print(lcm(12, 15))
    assert(lcm(12, 15) == 60)
    print(count_steps("input_P2_test.txt"))
    print(count_steps("input_P1.txt"))


if __name__ == "__main__":
    main()
