list_1 = list()
list_2 = list()
with open("input.txt", "r") as input:
    for row in input:
        row = row.strip()
        l1, l2 = row.split("  ")
        list_1.append(int(l1))
        list_2.append(int(l2))

list_1.sort()
list_2.sort()

print(sum([abs(x - y) for x, y in zip(list_1, list_2)]))
