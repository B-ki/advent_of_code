from collections import defaultdict


def create_complex_number_dict(input_file: str) -> dict:
    """
    Create a dict of complex number representing the grid
    """
    data = {}
    for x, row in enumerate(open(input_file)):
        for y, letter in enumerate(row.strip()):
            data[y + x * 1j] = letter
    return data


def find(pos: complex, union_find: dict) -> complex:
    """
    Find the root of a cell
    """
    if pos not in union_find:
        union_find[pos] = pos
    if union_find[pos] != pos:
        union_find[pos] = find(union_find[pos], union_find)
    return union_find[pos]


def union(pos1: complex, pos2: complex, union_find: dict) -> None:
    """
    Union two cells
    """
    union_find[find(pos1, union_find)] = find(pos2, union_find)


def get_area(cell_list: list | set) -> int:
    """
    Get the area of a component
    """
    return len(cell_list)


def get_perimeter(cell_list: list | set) -> set:
    """
    Get a list of tuple for cells at the perimeter of a component
    with p as the cell and d as the direction
    """
    return {(p, d) for d in [1, -1, 1j, -1j] for p in cell_list if p + d not in cell_list}


def P1_score(areas: list, perimeters: list) -> int:
    """
    Get the score for part 1
    """
    return sum(area * len(perimeter) for area, perimeter in zip(areas, perimeters))


def P2_score(areas: list, perimeters: list) -> int:
    """
    Get the score for part 2
    """
    return sum(area * len(perimeter - {(p + 1j * d, d) for p, d in perimeter}) for area, perimeter in zip(areas, perimeters))


def print_components(components: dict, data: dict) -> None:
    """
    Print the components
    """
    for source, cell_list in components.items() :
        print(
                "Value :", data[source], 
                " - Cells :", cell_list, 
                " \n  - Area :", get_area(cell_list),
                " \n  - Perimeters :", get_perimeter(cell_list)
            )


def main():
    data = create_complex_number_dict("input.txt")
    print(data)

    union_find: dict = {}
    for source in data:
        find(source, union_find) # iniating union_find, each cell is its own root
        for neighbour in [source + 1, source - 1, source + 1j, source -1j]:
            if neighbour in data and data[neighbour] == data[source]:
                union(source, neighbour, union_find)

    components = defaultdict(set)
    for source, component in union_find.items():
        components[find(source, union_find)].add(source)

    areas = [get_area(component) for component in components.values()]
    perimeters = [get_perimeter(component) for component in components.values()]

    print("Part 1 :", P1_score(areas, perimeters))
    print("Part 2 :", P2_score(areas, perimeters))


if __name__ == '__main__':
    main()



