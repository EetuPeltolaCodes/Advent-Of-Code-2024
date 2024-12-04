import re
import numpy as np

with open('Day-4\input.txt') as f:
    data = f.read()
    
data = data.split('\n')
data = np.array([list(x) for x in data])
rows, cols = data.shape

finds = 0

for x in range(1,rows - 1):
    for y in range(1, cols - 1):
        try:
            if data[x-1][y+1] == 'M' and data[x][y] == 'A' and data[x+1][y-1] == 'S' and data[x+1][y+1] == 'M' and data[x-1][y-1] == 'S':
                finds += 1
                #print('Found X-MAS at', x, y)
        except:
            pass
        
        try:
            if data[x-1][y+1] == 'M' and data[x][y] == 'A' and data[x+1][y-1] == 'S' and data[x+1][y+1] == 'S' and data[x-1][y-1] == 'M':
                finds += 1
                #print('Found X-MAS at', x, y)
        except:
            pass
        try:
            if data[x-1][y+1] == 'S' and data[x][y] == 'A' and data[x+1][y-1] == 'M' and data[x+1][y+1] == 'M' and data[x-1][y-1] == 'S':
                finds += 1
                #print('Found X-MAS at', x, y)
        except:
            pass
        
        try:
            if data[x-1][y+1] == 'S' and data[x][y] == 'A' and data[x+1][y-1] == 'M' and data[x+1][y+1] == 'S' and data[x-1][y-1] == 'M':
                finds += 1
                #print('Found X-MAS at', x, y)
        except:
            pass
            
            
print(f'Found {finds} instances of X-MAS in the data.')