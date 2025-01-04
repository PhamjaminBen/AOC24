import os

DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(row, col, map, visited: list = []):
    # print(row,col,visited)
    visited = visited.copy()
    visited.append((row, col))
    curr_num = map[row][col]
    if curr_num == 9:
        # print([(row,col,map[row][col]) for row,col in visited])
        return {(row, col)}

    num_paths = set()
    for drow, dcol in DIRECTIONS:
        new_row = row + drow
        new_col = col + dcol
        if (new_row, new_col) in visited:
            continue

        if 0 <= new_row < len(map) and 0 <= new_col < len(map[0]):
            if map[new_row][new_col] - 1 == curr_num:
                num_paths |= bfs(new_row, new_col, map, visited)

    return num_paths


with open(f"{os.path.dirname(__file__)}/input.txt") as file:
    map = [[int(y) for y in x.strip()] for x in file.readlines()]

    ret = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                ret += len(bfs(i, j, map))

    print(ret)
