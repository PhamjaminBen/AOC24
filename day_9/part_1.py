import os

with open(f"{os.path.dirname(__file__)}/input.txt") as file:
    inp = file.readlines()[0].strip()
    
    curr_id = 0

    map = []
    empty = []

    for i in range(len(inp)):
        num = int(inp[i])
        if i%2 == 0:
            map += [str(curr_id)]*num
            curr_id += 1
        else:
            prev_len = len(map)
            map += '.'*num
            empty.extend([prev_len+x for x in range(num)])
    
    map = list(map)
    for i in range(len(map)-1,-1,-1):
        if i < empty[0]: 
            break
        if map[i] != '.':
            new_idx = empty[0]
            map[new_idx] = map[i]
            map[i] = '.'
            empty.pop(0)
        
    print(sum([i*int(x) for i,x in enumerate(map) if x != '.']))
