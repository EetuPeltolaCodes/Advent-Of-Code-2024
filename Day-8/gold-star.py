import numpy as np
import re
import itertools

with open('Day-8/input.txt') as f:
    data = f.read().splitlines()
antenna_coordinates = {}
row = 0
for line in data:
    col = 0
    for node in line:
        if re.search(r'\d', node):
            try:
                antenna_type = re.findall(r'\d', node)[0]
                antenna_coordinates[antenna_type].append((row, col))
            except:
                antenna_type = re.findall(r'\d', node)[0]
                antenna_coordinates.update({antenna_type: [(row, col)]})
        if re.search(r'[a-zA-Z]', node):
            try:
                antenna_type = re.findall(r'[a-zA-Z]', node)[0]
                antenna_coordinates[antenna_type].append((row, col))
            except:
                antenna_type = re.findall(r'[a-zA-Z]', node)[0]
                antenna_coordinates.update({antenna_type: [(row, col)]})
        col += 1
    row += 1
boundary_x = row
boundary_y = col   
antinodes = 0
antenna_types = list(antenna_coordinates.keys())
antinode_coordinates = set()
for antenna_type in antenna_types:
    combinations = list(itertools.combinations(antenna_coordinates[antenna_type], 2))
    for combination in combinations:
        x1, y1 = combination[0]
        x2, y2 = combination[1]
        
        dx = x2 - x1
        dy = y2 - y1
        new_x1 = x1 - dx
        new_x2 = x2 + dx
        new_y1 = y1 - dy
        new_y2 = y2 + dy
        
        while (new_x1 >= 0 and new_x1 < boundary_x and new_y1 >= 0 and new_y1 < boundary_y):
        
            if (new_x1, new_y1) not in antinode_coordinates:
                antinodes += 1
                antinode_coordinates.add((new_x1, new_y1))
            
            new_x1 -= dx
            new_y1 -= dy
            
        
        while (new_x2 >= 0 and new_x2 < boundary_x and new_y2 >= 0 and new_y2 < boundary_y):
            
            if (new_x2, new_y2) not in antinode_coordinates:
                antinodes += 1
                antinode_coordinates.add((new_x2, new_y2))
            
            new_x2 += dx
            new_y2 += dy

for antenna_type in antenna_types:
    for x, y in antenna_coordinates[antenna_type]:
        if (x, y) not in antinode_coordinates:
            antinodes += 1
            antinode_coordinates.add((x, y))           
                    
print(f'There are {antinodes} antinodes')
