import random

def silnik(len : int) -> list[int]:
    nums = []
    for i in range(len):
        nums.append(random.randint(0, 9))

    return nums