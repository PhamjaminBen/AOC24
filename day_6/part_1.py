import os

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    raw = f.readlines()
    map = [list(line.strip()) for line in raw]

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                start_row, start_col = i, j
                break

    curr_row, curr_col = start_row, start_col

    visited = set()
    curr_direction_idx = 0
    curr_direction = DIRECTIONS[curr_direction_idx]

    while True:
        visited.add((curr_row, curr_col))
        new_row = curr_row + curr_direction[0]
        new_col = curr_col + curr_direction[1]

        # Exit when out of bounds detected
        if not (0 <= new_row < len(map) and 0 <= new_col < len(map[0])):
            break

        try:
            if map[new_row][new_col] == "#":
                curr_direction_idx = (curr_direction_idx + 1) % 4
                curr_direction = DIRECTIONS[curr_direction_idx]
            else:
                curr_row = new_row
                curr_col = new_col
        except:
            break

    print(len(visited))
