

def main():
    path = "test"
    seeds_file = open(f"../{path}/seeds", 'r')
    seed_to_soil_file = open(f"../{path}/seed-to-soil", 'r')
    soil_to_fert_file = open(f"../{path}/soil-to-fertilizer", 'r')
    fert_to_water_file = open(f"../test/fertilizer-to-water", 'r')
    water_to_light_file = open(f"../test/water-to-light", 'r')
    light_to_temperature_file = open(f"../test/light-to-temperature", 'r')
    temperature_to_humidity_file = open(f"../test/temperature-to-humidity", 'r')
    humidity_to_location_file = open(f"../test/humidity-to-location", 'r')
    seeds = seeds_file.readline()
    seed_to_soil_map = seed_to_soil_file.readline()
    soil_to_fert_map = soil_to_fert_file.readline()
    fert_to_water_map = fert_to_water_file.readline()
    water_to_light_map = water_to_light_file.readline()
    light_to_temperature_map = light_to_temperature_file.readline()
    temperature_to_humidity_map = temperature_to_humidity_file.readline()
    humidity_to_location_map = humidity_to_location_file.readline()


if __name__ == '__main__':
    main()
