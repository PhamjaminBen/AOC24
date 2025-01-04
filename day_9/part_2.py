import os

with open(f"{os.path.dirname(__file__)}/input.txt") as file:
    inp = file.readlines()[0].strip()

    curr_id = 0

    map_len = 0
    full = []
    empty = []

    for i in range(len(inp)):
        num = int(inp[i])
        if i % 2 == 0:
            full.append([map_len, num, curr_id])
            curr_id += 1
        else:
            empty.append([map_len, num])

        map_len += num

    # Checking each full block and finding earliest block it can fit into
    for i in range(len(full) - 1, -1, -1):
        start, length, id = full[i]
        for j in range(0, len(empty)):
            # Don't allow block to move further back
            if start < empty[j][0]:
                break

            # Update empty block
            if length < empty[j][1]:
                full[i][0] = empty[j][0]
                empty[j][0] += length
                empty[j][1] -= length
                break
            # Remove empty block
            elif length == empty[j][1]:
                full[i][0] = empty[j][0]
                empty.pop(j)
                break

    check_sum = 0
    for start, len, id in full:
        check_sum += sum([x * id for x in range(start, start + len)])

    print(check_sum)
