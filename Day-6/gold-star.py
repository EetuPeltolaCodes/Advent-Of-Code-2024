import re
import time

MAX_COUNT = 1000

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
start_position = current_position
start_direction = current_direction
visited = []
data = [list(line) for line in data]
while True:
    if current_position[0] < 0 or current_position[1] < 0 or current_position[0] >= len(data) or current_position[1] >= len(data[0]):
            break
    visited.append(current_position)
    match current_direction:
        case '^':
            try:
                infront = [current_position[0] - 1, current_position[1]]
                if data[infront[0]][infront[1]] == '#':
                    current_direction = '>'
                    #current_position = [current_position[0], current_position[1] + 1]
                else:
                    current_position = infront
            except IndexError:
                break
        case 'v':
            try:
                infront = [current_position[0] + 1, current_position[1]]
                if data[infront[0]][infront[1]] == '#':
                    current_direction = '<'
                    #current_position = [current_position[0], current_position[1] - 1]
                else:
                    current_position = infront
            except IndexError:
                data[current_position[0]][current_position[1]] = 'X'
                break
        case '<':
            try:
                infront = [current_position[0], current_position[1] - 1]
                if data[infront[0]][infront[1]] == '#':
                    current_direction = '^'
                    #current_position = [current_position[0] - 1, current_position[1]]
                else:
                    current_position = infront
            except IndexError:
                break
        case '>':
            try:
                infront = [current_position[0], current_position[1] + 1]
                if data[infront[0]][infront[1]] == '#':
                    current_direction = 'v'
                    #current_position = [current_position[0] + 1, current_position[1]]
                else:
                    current_position = infront
            except IndexError:
                break         

time1 = time.time()
iterations = 0
visited2 = []
for visit in visited:
    if visit not in visited2:
        visited2.append(visit)
visited = visited2
paradoxes = 0
paradox_positions = []
for visit in visited:
    current_position = start_position[:]
    current_direction = start_direction
    new_obstacle = visit
    visited_states = set()
    count = 0

    grid_copy = [row[:] for row in data]
    grid_copy[new_obstacle[0]][new_obstacle[1]] = '#'

    while True:
        if current_position[0] < 0 or current_position[1] < 0 or \
           current_position[0] >= len(grid_copy) or current_position[1] >= len(grid_copy[0]):
            break
        
        state = (current_position[0], current_position[1], current_direction)
        if state in visited_states:
            count += 1
            if count > MAX_COUNT:
                paradoxes += 1
                paradox_positions.append(new_obstacle)
                break
        else:
            visited_states.add(state)
        
        match current_direction:
            case '^':
                infront = [current_position[0] - 1, current_position[1]]
                if infront[0] < 0:
                    break
                if grid_copy[infront[0]][infront[1]] == '#':
                    current_direction = '>'
                    #current_position[1] += 1
                else:
                    current_position = infront
            case 'v':
                infront = [current_position[0] + 1, current_position[1]]
                if infront[0] >= len(grid_copy):
                    break
                if  grid_copy[infront[0]][infront[1]] == '#':
                    current_direction = '<'
                    #current_position[1] -= 1
                else:
                    current_position = infront
            case '<':
                infront = [current_position[0], current_position[1] - 1]
                if infront[1] < 0:
                    break
                if grid_copy[infront[0]][infront[1]] == '#':
                    current_direction = '^'
                    #current_position[0] -= 1
                else:
                    current_position = infront
            case '>':
                infront = [current_position[0], current_position[1] + 1]
                if infront[1] >= len(grid_copy):
                    break
                if  grid_copy[infront[0]][infront[1]] == '#':
                    current_direction = 'v'
                    #current_position[0] += 1
                else:
                    current_position = infront
       
    iterations += 1
    if iterations % 100 == 0:
        print(f'Iterations: {iterations}')  
                    
time2 = time.time()
print(f'Time taken: {(time2 - time1):.4f} seconds.')          
                    
print(f'There are {paradoxes} ways to get paradoxes.')
            