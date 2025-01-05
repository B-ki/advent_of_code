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
    if pos not in union_find:
        union_find[pos] = pos
    if union_find[pos] != pos:
        union_find[pos] = find(union_find[pos], union_find)
    return union_find[pos]


def union(pos1: complex, pos2: complex, union_find: dict) -> None:
    union_find[find(pos1, union_find)] = find(pos2, union_find)


def main():
    data = create_complex_number_dict("input.txt")
    print(data)

    union_find: dict = {}
    for source in data:
        find(source, union_find) # iniating union_find, each cell is its own root
        for neighbour in [source + 1, source - 1, source + 1j, source -1j]:
            if neighbour in data and data[neighbour] == data[source]:
                union(source, neighbour, union_find)
    #print("Union_find]\n", union_find)

    components = defaultdict(set)
    for source, component in union_find.items():
        components[find(source, union_find)].add(source)
    #print("Components\n", components)
    for source, cell_list in components.items() :
        print(
                "Value :", data[source], 
                " - Cells :", cell_list, 
                " \n  - Area :", len(cell_list),
                " \n  - Perimeters :", {(p, d) for d in [1, -1, 1j, -1j] for p in cell_list if p + d not in cell_list}
            )
    areas = [len(component) for component in components.values()]
    perimeters = [{(p, d) for d in [1, -1, 1j, -1j] for p in c if p + d not in c} for c in components.values()]

    print("P1", sum(area * len(perimeter) for area, perimeter in zip(areas, perimeters)))
    print(
        "P2",
        sum(area * len(perimeter - {(p + 1j * d, d) for p, d in perimeter}) for area, perimeter in zip(areas, perimeters))
    )



if __name__ == '__main__':
    main()



