import numpy as np
with open('Day-9\input.txt') as f:
    data = f.read()
    i = 0
    disk = []
    for j in range(1,len(data)+1):
        if np.mod(j,2) == 0:
            for k in range(0,int(data[j-1])):
                disk.append('.')
        else:
            for k in range(0,int(data[j-1])):
                disk.append(i)
            i += 1      
    upside_down = disk[::-1]
    points = []
    # Find all the '.' indexes in the disk
    for i in range(0,len(disk)):
        if disk[i] == '.':
            points.append(i)     
    n = 0
    num = 0
    for i in range(0,len(disk)):
        help = True
        if (len(disk)-n) >= points[0]:
            help = False
        if help:
            if np.mod(len(disk),2) == 0:
                disk = disk[: (len(disk) - n)]
            else:
                disk = disk[: (len(disk) - (n - 1))]
            break
        if i in points:
            if upside_down[n] == '.':
                while upside_down[n] == '.':
                    n += 1
                disk[i] = upside_down[n]
                num = upside_down[n]
                n += 1
                points.pop(0) 
            else:
                disk[i] = upside_down[n]
                num = upside_down[n]
                n += 1  
                points.pop(0)        
    checksum = 0
    for i in range(0,len(disk)):
        checksum += i*int(disk[i])
    
    print(f'The filesystem checksum is: {checksum}')
    
    #6259790630969 last [5247, 5247, 5247, 5247, 5246, 5246, 5246, 5246, 5246]
    # Got 6259530434615 last 