from functools import lru_cache
BLINKS = 75

@lru_cache(maxsize=None)
def count_stone(stone, depth):
    if stone == 0:
        first = 1
        second = None
    elif len(str(stone)) % 2 == 0:
        index = len(str(stone)) // 2
        first = int(str(stone)[:index])
        second = int(str(stone)[index:])
    else:
        first = stone*2024
        second = None
        
    if depth == BLINKS:
        if second is not None:
            return 2
        else:
            return 1
    number_of_stones = count_stone(first, depth+1)
    if second is not None:
        number_of_stones += count_stone(second, depth+1)
    return number_of_stones
        

with open('Day-11\input.txt') as f:
    data = f.read().split(' ')
    data = [int(i) for i in data]
    number_of_stones = 0
    for i in range(0,len(data)):
        number = data[i]
        number_of_stones += count_stone(number, 1)
    print(f'There are {number_of_stones} stones after {BLINKS} blinks')