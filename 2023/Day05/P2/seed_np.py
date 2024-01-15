from typing import Any, List
import numpy as np
from numpy._typing import NDArray

def read_matrix_from_file_path(file_path: str) -> np.ndarray:
    '''create a matrix from a file'''
    matrix: NDArray[Any] = np.loadtxt(file_path, dtype=int)
    return matrix

def translate_with_mat(value: int, mat: np.ndarray) -> int:
    '''get a dest value from a map'''
    for row in mat:
        if value >= row[1] and value < row[1] + row[2]:
            return value - row[1] + row[0]
    return value

def seed_to_location(value: int, matrixes: List[np.ndarray]) -> int:
    '''get the location from one seed'''
    result = value
    for matrix in matrixes:
        result = translate_with_mat(result, matrix)
    return result

def create_seed(seeds: np.ndarray) -> List[List[int]]:
    '''create all seed list for P2'''
    res: List[List[int]] = []
    for s0, s1 in zip(seeds[::2], seeds[1::2]):
        res.append([s0, s0 + s1 - 1])
    return res

def optimize_path_translation(seed_ranges: List[List[int]], all_map: List[np.ndarray]) -> int:
    '''get the optimized path'''
    for mat in all_map:
        print("\n### NEW MAP ###")
        # print("map: ", map)
        transformed: List[List[int]] = []
        for l in mat:
            print("map line: ", l, "seed_ranges: ", seed_ranges)
            dest, src, r = l[0], l[1], l[2]
            untransformed: List[List[int]] = []
            while seed_ranges:
                elem = seed_ranges.pop()
                start, end = elem[0], elem[1]
                before = [start, min(end, src - 1)]
                inter = [max(start, src), min(end, src + r)]
                after = [max(src + r + 1, start), end]
                if before[1] >= before[0]:
                    untransformed.append(before)
                if inter[1] >= inter[0]:
                    print("inter: ", inter)
                    transformed.append([inter[0] + dest - src, inter[1] - src + dest])
                if after[1] >= after[0]:
                    untransformed.append(after)
            seed_ranges = untransformed
            print("transformed: ", transformed)
            print("untransformed: ", untransformed)
        seed_ranges = seed_ranges + transformed
    print(seed_ranges)
    min_values: List[int] = []
    for e in seed_ranges:
        min_values.append(e[0])
    return min(min_values)

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

    seeds = np.loadtxt(seeds_file_path, dtype=int)
    print(seeds, seeds.shape)
    seed_to_soil_mat = read_matrix_from_file_path(seed_to_soil_file_path)
    soil_to_fert_mat = read_matrix_from_file_path(soil_to_fert_file_path)
    fert_to_water_mat = read_matrix_from_file_path(fert_to_water_file_path)
    water_to_light_mat = read_matrix_from_file_path(water_to_light_file_path)
    light_to_temperature_mat = read_matrix_from_file_path(light_to_temperature_file_path)
    temperature_to_humidity_mat = read_matrix_from_file_path(temperature_to_humidity_file_path)
    humidity_to_location_mat = read_matrix_from_file_path(humidity_to_location_file_path)
    print(seed_to_soil_mat, seed_to_soil_mat.shape)
    print(soil_to_fert_mat, soil_to_fert_mat.shape)
    print(fert_to_water_mat, fert_to_water_mat.shape)
    print(water_to_light_mat, water_to_light_mat.shape)
    print(light_to_temperature_mat, light_to_temperature_mat.shape)
    print(temperature_to_humidity_mat, temperature_to_humidity_mat.shape)
    print(humidity_to_location_mat, humidity_to_location_mat.shape)
 
    all_map =[seed_to_soil_mat, soil_to_fert_mat, fert_to_water_mat,
                        water_to_light_mat, light_to_temperature_mat,
                        temperature_to_humidity_mat, humidity_to_location_mat]

    seed_ranges = create_seed(seeds)
    min_location = optimize_path_translation(seed_ranges, all_map)
    print("\nANSWER = ", min_location)

if __name__ == '__main__':
    main()

