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


def browse_dict_map(dict_map: dict, directions: str) -> int:
    """
    Browse the adjacency list according to the directions
    """
    current_node = "AAA"
    
    i = 0
    while current_node != "ZZZ":
        for direction in directions:
            if current_node == "ZZZ":
                return i
            if direction == "L":
                direction_int = 0
            else:
                direction_int = 1
            current_node = dict_map[current_node][direction_int]
            i+=1
    return i


def count_steps(file_path: str) -> int:
    """
    Count the number of steps to reach the end
    """
    input_lines = get_input(file_path)
    directions, map_list = treat_input(input_lines) 
    dict_map = create_adjacency_list(map_list)
    return browse_dict_map(dict_map, directions)


def main():
    print(count_steps("input_test.txt"))
    print(count_steps("input_test2.txt"))
    print(count_steps("input_P1.txt"))


if __name__ == "__main__":
    main()
