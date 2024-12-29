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

    # Finding start position
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                start_row, start_col = i, j
                break

    # checks if an infinite loops is reached
    def check_infinite(row, col, curr_direction_idx, visited: list):
        curr_row, curr_col = row, col
        new_visited = visited.copy()
        curr_direction = DIRECTIONS[curr_direction_idx]

        while 0 <= curr_row < len(map) and 0 <= curr_col < len(map[0]):
            new_row = curr_row + curr_direction[0]
            new_col = curr_col + curr_direction[1]
            if not (0 <= new_row < len(map) and 0 <= new_col < len(map[0])):
                return False

            # if in same spot and same direction twice, infinite loop
            if ((curr_row, curr_col), curr_direction_idx) in new_visited:
                return True
            new_visited.append(((curr_row, curr_col), curr_direction_idx))

            if map[new_row][new_col] == "#":
                curr_direction_idx = (curr_direction_idx + 1) % 4
                curr_direction = DIRECTIONS[curr_direction_idx]
                new_visited.pop()
            else:
                curr_row = new_row
                curr_col = new_col

        return False

    obs_count = 0

    # in this step, we simulate placing an obstruction in front of every single step and see if it results in an infinite loop
    curr_row, curr_col = start_row, start_col
    curr_direction_idx = 0
    curr_direction = DIRECTIONS[curr_direction_idx]
    visited = list()

    while 0 <= curr_row < len(map) and 0 <= curr_col < len(map[0]):
        if len(visited) % 100 == 0:
            print("visited", len(visited), "obs count", obs_count)
        new_row = curr_row + curr_direction[0]
        new_col = curr_col + curr_direction[1]

        if not (0 <= new_row < len(map) and 0 <= new_col < len(map[0])):
            break

        visited.append(((curr_row, curr_col), curr_direction_idx))

        if map[new_row][new_col] == "#":
            curr_direction_idx = (curr_direction_idx + 1) % 4
            curr_direction = DIRECTIONS[curr_direction_idx]
            visited.pop()
        else:
            # if obstruction interferes with previous path, do not consider it
            if not {((new_row, new_col), dir) for dir in range(4)} & set(visited[:-1]):
                map[new_row][new_col] = "#"
                if check_infinite(curr_row, curr_col, curr_direction_idx, visited[:-1]):
                    obs_count += 1

                map[new_row][new_col] = "."

            curr_row = new_row
            curr_col = new_col

    print(obs_count)
