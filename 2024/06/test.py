import numpy as np

# Convert the map into a NumPy array
map_list = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]
map_array = np.array([list(row) for row in map_list])

# Modify the map
row_index, col_index = 2, 5  # Example position to replace
map_array[row_index, col_index] = 'X'

# Print the modified map
for row in map_array:
    print(''.join(row))
