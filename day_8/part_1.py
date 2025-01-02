import os
from collections import defaultdict


with open(f"{os.path.dirname(__file__)}/input.txt") as file:
    map = [list(line.strip()) for line in file.readlines()]

    nodes_dict = defaultdict(list)
    antinodes = set()

    for row in range(len(map)):
        for col in range(len(map[0])):
            tile = map[row][col]
            if tile != ".":
                nodes_dict[tile].append((row, col))

    for antennas in nodes_dict.values():
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                att1 = antennas[i]
                att2 = antennas[j]

                diff = (att1[0] - att2[0], att1[1] - att2[1])

                atn1 = (att1[0] + diff[0], att1[1] + diff[1])
                atn2 = (att2[0] - diff[0], att2[1] - diff[1])

                if 0 <= atn1[0] < len(map) and 0 <= atn1[1] < len(map[0]):
                    antinodes.add(atn1)

                if 0 <= atn2[0] < len(map) and 0 <= atn2[1] < len(map[0]):
                    antinodes.add(atn2)

    print(len(antinodes))
