import random

# returns list of digits, number of digits = len
def silnik(len : int) -> list[int]:
    nums = []
    for i in range(len):
        nums.append(random.randint(0, 9))

    return nums