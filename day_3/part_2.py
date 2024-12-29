import re

file = "input.txt"

with open(file, "r") as input:
    data = [x.strip() for x in input.readlines()]
    text = "".join(data)

    multi_pairs = re.findall(r"mul\((\d*),(\d*)\)|(do\(\)|don\'t\(\))", text)

    sum = 0
    enabled = True
    for num_1, num_2, instruction in multi_pairs:
        if instruction == "don't()":
            enabled = False

        elif instruction == "do()":
            enabled = True

        elif enabled:
            sum += int(num_1) * int(num_2)

    print(sum)
