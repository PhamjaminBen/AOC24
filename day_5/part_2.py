from collections import defaultdict
import os

def fix_update(update: list, before_dict: defaultdict[set]):
    remaining_nums = set(update)
    new_update = list()
    while len(remaining_nums) > 0:
        for num in remaining_nums:
            if not before_dict[num] & remaining_nums:
                new_update.append(num)
                remaining_nums.remove(num)
                break

    return int(new_update[len(new_update) // 2])


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
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
                middle_sum += fix_update(update, before_dict)
                break

    print(middle_sum)
