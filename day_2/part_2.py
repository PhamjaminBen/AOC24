def calculate_safe(level):
    increasing = (level[1] - level[0]) > 0
    for i in range(len(level) - 1):
        diff = level[i + 1] - level[i]

        if diff == 0:
            return False

        if (diff > 0) != increasing:
            return False

        if abs(diff) > 3 or abs(diff) < 1:
            return False

    return True


safe_count = 0
sol_1 = set()
sol_2 = set()

with open("input.txt", "r") as input:
    for line in input:
        level = [int(x) for x in line.strip().split(" ")]

        if calculate_safe(level):
            safe_count += 1
            continue

        for i in range(len(level)):
            modified = level.copy()
            modified.pop(i)
            if calculate_safe(modified):
                sol_1.add(tuple(level))
                safe_count += 1
                break

print(safe_count)
