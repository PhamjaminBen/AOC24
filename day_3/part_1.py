import re

file = "test.txt"

with open(file, "r") as input:
    data = [x.strip() for x in input.readlines()]
    text = "".join(data)

    multi_pairs = re.findall(r"mul\((\d*),(\d*)\)", text)

    print(sum([int(x) * int(y) for x, y in multi_pairs]))
