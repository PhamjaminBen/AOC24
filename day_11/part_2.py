import os

memo_dict = {}


def next_stone(num, step=0):
    if (num, step) in memo_dict:
        return memo_dict[(num, step)]
    num = str(int(num))
    if step == 75:
        return 1

    if num == "0":
        ans = next_stone("1", step + 1)

    elif len(num) % 2 == 0:
        ans = next_stone(num[: len(num) // 2], step + 1) + next_stone(
            num[len(num) // 2 :], step + 1
        )
    else:
        ans = next_stone(str(int(num) * 2024), step + 1)

    memo_dict[(num, step)] = ans
    return ans


with open(f"{os.path.dirname(__file__)}/input.txt") as file:
    stones = file.readlines()[0].strip().split(" ")
    print(sum([next_stone(stone) for stone in stones]))
