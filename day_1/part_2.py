from collections import defaultdict

list_1 = list()
list_2_count = defaultdict(int)
with open("input.txt", "r") as input:
    for row in input:
        l1, l2 = row.strip().split("  ")
        list_1.append(int(l1))
        list_2_count[int(l2)] += 1

print(sum([num * list_2_count[num] for num in list_1]))
