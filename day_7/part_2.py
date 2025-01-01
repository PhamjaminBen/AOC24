import os


def find_solution(target, curr, remaining_nums: tuple):
    if not remaining_nums:
        if curr == target:
            return True
        else:
            return False

    return (
        find_solution(target, curr + remaining_nums[0], remaining_nums[1:])
        or find_solution(target, curr * remaining_nums[0], remaining_nums[1:])
        or find_solution(target, int(f"{curr}{remaining_nums[0]}"), remaining_nums[1:])
    )


result = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as file:
    raw = file.readlines()

    for line in raw:
        total, numbers = line.strip().split(": ")
        total = int(total)

        numbers = tuple([int(num) for num in numbers.split(" ")])

        if find_solution(total, numbers[0], numbers[1:]):
            result += total

    print(result)
