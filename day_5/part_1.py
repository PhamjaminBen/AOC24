from collections import defaultdict

with open("day_5/input.txt") as f:
    raw = f.readlines()

    curr_line = 0

    before_dict = defaultdict(set)

    while True:
        line = raw[curr_line].strip()
        if not line:
            break
        else:
            num_1, num_2 = line.split("|")
            before_dict[num_1].add(num_2)

        curr_line += 1

    middle_sum = 0

    for update in raw[curr_line + 1 :]:
        update = update.strip().split(",")

        seen = set()
        for num in update:
            seen.add(num)
            if seen & before_dict[num]:
                break
        else:
            middle_sum += int(update[len(update) // 2])

    print(middle_sum)
