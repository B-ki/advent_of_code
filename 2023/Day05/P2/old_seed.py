from typing import List


def read_matrix_from_file_path(file_path: str) -> List[List[int]]:
    '''create a matrix from a file'''
    matrix: List[List[int]] = []

    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.split()]
            matrix.append(row)

    return matrix

def translate_with_mat(value: int, mat: List[List[int]]) -> int:
    '''get a dest value from a map'''
    for l in mat:
        if value >= l[1] and value < l[1] + l[2]:
            return value - l[1] + l[0]
    return value

def seed_to_location(value: int, matrixes: List[List[List[int]]]) -> int:
    '''get the location from one seed'''
    result = value
    for matrix in matrixes:
        result = translate_with_mat(result, matrix)
    return result

def create_seed(seeds: List[int]) -> List[int]:
    '''create all seed list for P2'''
    res: List[int] = []
    for i in range(len(seeds)):
        if i % 2 == 1:
            pass
        else:
            for j in range(seeds[i + 1]):
                res.append(seeds[i] + j)
    return res

def main():
    path = "input"
    seeds_file_path = f"../{path}/seeds"
    seed_to_soil_file_path = f"../{path}/seed-to-soil"
    soil_to_fert_file_path = f"../{path}/soil-to-fertilizer"
    fert_to_water_file_path = f"../{path}/fertilizer-to-water"
    water_to_light_file_path = f"../{path}/water-to-light"
    light_to_temperature_file_path = f"../{path}/light-to-temperature"
    temperature_to_humidity_file_path = f"../{path}/temperature-to-humidity"
    humidity_to_location_file_path = f"../{path}/humidity-to-location"
    seeds = open(seeds_file_path, 'r').readline().split()
    seeds = [int(x) for x in seeds]
    seed_to_soil_mat = read_matrix_from_file_path(seed_to_soil_file_path)
    soil_to_fert_mat = read_matrix_from_file_path(soil_to_fert_file_path) 
    fert_to_water_mat = read_matrix_from_file_path(fert_to_water_file_path)
    water_to_light_mat = read_matrix_from_file_path(water_to_light_file_path)
    light_to_temperature_mat = read_matrix_from_file_path(light_to_temperature_file_path)
    temperature_to_humidity_mat = read_matrix_from_file_path(temperature_to_humidity_file_path)
    humidity_to_location_mat = read_matrix_from_file_path(humidity_to_location_file_path)
    all_map = [seed_to_soil_mat, soil_to_fert_mat, fert_to_water_mat,
                water_to_light_mat, light_to_temperature_mat, 
                temperature_to_humidity_mat, humidity_to_location_mat]
    print(seeds)
    seeds_P2 = create_seed(seeds)
    print(seed_to_soil_mat)
    print(soil_to_fert_mat)
    print(fert_to_water_mat)
    print(water_to_light_mat)
    print(light_to_temperature_mat)
    print(temperature_to_humidity_mat)
    print(humidity_to_location_mat)
    locations: List[int] = []
    for s in seeds_P2:
        locations.append(seed_to_location(int(s), all_map))
    print(locations)
    print(min(locations))


if __name__ == '__main__':
    main()
