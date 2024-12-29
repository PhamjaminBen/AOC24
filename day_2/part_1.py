safe_count = 0

with open("input.txt", "r") as input:
    for line in input:
        level = [int(x) for x in line.strip().split(" ")]

        increasing = level[1] - level[0] > 0

        for i in range(len(level) - 1):
            diff = level[i + 1] - level[i]

            if diff == 0:
                break

            if (diff > 0) != increasing:
                break

            if abs(diff) > 3 or abs(diff) < 1:
                break

        else:
            safe_count += 1

print(safe_count)
