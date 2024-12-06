import re

with open('Day-6\input.txt', 'r') as f:
    lines = f.readlines()
    data = [line.strip() for line in lines]
    
    directions = ['^', 'v', '<', '>']
    
    for direction in directions:
        current_position = [0, 0]
        for x in data:
            check = re.search(r"" + re.escape(direction), x)
            if check:
                current_index = x.index(direction)
                current_direction = direction
                current_position = [current_position[0], current_position[1] + current_index]
                break
            current_position = [current_position[0] + 1, current_position[1]]
        if current_position != [0, 0]:
            break

    data = [list(line) for line in data]
    while True:
        match current_direction:
            case '^':
                try:
                    infront = [current_position[0] - 1, current_position[1]]
                    if data[infront[0]][infront[1]] == '#':
                        current_direction = '>'
                        data[current_position[0]][current_position[1]] = 'X'
                        current_position = [current_position[0], current_position[1] + 1]
                    else:
                        data[current_position[0]][current_position[1]] = 'X'
                        current_position = infront
                except:
                    data[current_position[0]][current_position[1]] = 'X'
                    break
            case 'v':
                try:
                    infront = [current_position[0] + 1, current_position[1]]
                    if data[infront[0]][infront[1]] == '#':
                        current_direction = '<'
                        data[current_position[0]][current_position[1]] = 'X'
                        current_position = [current_position[0], current_position[1] - 1]
                    else:
                        data[current_position[0]][current_position[1]] = 'X'
                        current_position = infront
                except:
                    data[current_position[0]][current_position[1]] = 'X'
                    break
            case '<':
                try:
                    infront = [current_position[0], current_position[1] - 1]
                    if data[infront[0]][infront[1]] == '#':
                        current_direction = '^'
                        data[current_position[0]][current_position[1]] = 'X'
                        current_position = [current_position[0] - 1, current_position[1]]
                    else:
                        data[current_position[0]][current_position[1]] = 'X'
                        current_position = infront
                except:
                    data[current_position[0]][current_position[1]] = 'X'
                    break
            case '>':
                try:
                    infront = [current_position[0], current_position[1] + 1]
                    if data[infront[0]][infront[1]] == '#':
                        current_direction = 'v'
                        data[current_position[0]][current_position[1]] = 'X'
                        current_position = [current_position[0] + 1, current_position[1]]
                    else:
                        data[current_position[0]][current_position[1]] = 'X'
                        current_position = infront
                except:
                    data[current_position[0]][current_position[1]] = 'X'
                    break
                
    data = [''.join(line) for line in data]
    sum_X = 0
    for x in data:
        sum_X += len(re.findall(r"X", x))

    print(f'There are {sum_X} positions the guard visited at least once.')
            