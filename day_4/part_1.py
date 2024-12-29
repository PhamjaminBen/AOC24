with open("input.txt", "r") as input:
    grid = [list(line.strip()) for line in input]


def find_matches(row, col):
    num_matches = 0

    directions = (
        ((1, 0), (2, 0), (3, 0)),
        ((-1, 0), (-2, 0), (-3, 0)),
        ((0, -1), (0, -2), (0, -3)),
        ((0, 1), (0, 2), (0, 3)),
        ((1, 1), (2, 2), (3, 3)),
        ((1, -1), (2, -2), (3, -3)),
        ((-1, 1), (-2, 2), (-3, 3)),
        ((-1, -1), (-2, -2), (-3, -3)),
    )

    for direction in directions:
        try:
            name = [
                grid[row + rx][col + ry]
                for rx, ry in direction
                if row + rx >= 0 and col + ry >= 0
            ]
            if name == ["M", "A", "S"]:
                num_matches += 1
        except:
            continue

    return num_matches


num_matches = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "X":
            num_matches += find_matches(row, col)

print(num_matches)
