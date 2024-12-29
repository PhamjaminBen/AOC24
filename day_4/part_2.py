with open("input.txt", "r") as input:
    grid = [list(line.strip()) for line in input]


def find_matches(row, col):
    num_matches = 0

    if row == 0 or col == 0:
        return 0

    try:
        if {grid[row + 1][col + 1], grid[row - 1][col - 1]} == {"M", "S"} and {
            grid[row + 1][col - 1],
            grid[row - 1][col + 1],
        } == {"M", "S"}:
            return 1
    except:
        return 0

    return num_matches


num_matches = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "A":
            num_matches += find_matches(row, col)

print(num_matches)
