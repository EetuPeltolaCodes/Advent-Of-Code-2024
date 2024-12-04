import re
import numpy as np
import pandas as pd

def search_horizontal(data):
    horizontal_finds = 0
    data = data.split('\n')
    for x in data:
        horizontal_finds += len(re.findall(r'XMAS', x)) + len(re.findall(r'SAMX', x))
        
    return horizontal_finds

def search_vertical(data):
    vertical_finds = 0
    data = data.split('\n')
    data = np.array([list(x) for x in data])
    data = pd.DataFrame(data)
    
    for x in range(len(data.columns)):
        vertical_finds += len(re.findall(r'XMAS', ''.join(data[x].to_list()))) + len(re.findall(r'SAMX', ''.join(data[x].to_list())))
        
    return vertical_finds

def search_diagonal(data):
    diagonal_finds = 0
    data = data.split('\n')
    data = np.array([list(x) for x in data])
    rows, cols = data.shape
    
    for x in range(rows - 3):
        for y in range(cols - 3):
            try:
                if data[x][y] == 'X' and data[x+1][y+1] == 'M' and data[x+2][y+2] == 'A' and data[x+3][y+3] == 'S':
                    diagonal_finds += 1
                    #print('Found XMAS at', x, y)
            except:
                pass
            
            try:
                if data[x][y] == 'S' and data[x+1][y+1] == 'A' and data[x+2][y+2] == 'M' and data[x+3][y+3] == 'X':
                    diagonal_finds += 1
                    #print('Found SAMX at', x, y)
            except:
                pass
    for x in range(rows - 3):
        for y in range(3, cols):
            if data[x][y] == 'X' and data[x+1][y-1] == 'M' and data[x+2][y-2] == 'A' and data[x+3][y-3] == 'S':
                diagonal_finds += 1
                #print('Found XMAS at', x, y)
            if data[x][y] == 'S' and data[x+1][y-1] == 'A' and data[x+2][y-2] == 'M' and data[x+3][y-3] == 'X':
                diagonal_finds += 1
                #print('Found SAMX at', x, y)
            
    return diagonal_finds

with open('Day-4\input.txt') as f:
    data = f.read()
    
horizontals = search_horizontal(data)
verticals = search_vertical(data)
diagonals = search_diagonal(data)
    
all_finds = horizontals + verticals + diagonals
print(f'The total number of XMAS found in the data is: {all_finds}')