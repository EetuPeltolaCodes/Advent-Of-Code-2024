import numpy as np
with open('Day-9\input.txt') as f:
    data = f.read()
    i = 0
    disk = []
    for j in range(1,len(data)+1):
        if np.mod(j,2) == 0:
            if int(data[j-1]) != 0:
                disk.append(('.', int(data[j-1])))
        else:
            if int(data[j-1]) != 0:
                disk.append((i, int(data[j-1])))
            i += 1      
    highest = i

    for k in range(1, len(disk)+1):
        n = - k
        for m in range(0, len(disk)+n):
            i, j = disk[m]
            if i == '.':
                i2, j2 = disk[n]
                dj = j-j2
                if dj == 0 and i2 != '.':
                    disk[m] = (i2, j2)
                    disk[n] = ('.', j2)
                    break
                elif dj > 0 and i2 != '.':
                    disk[m] = (i2, j2)
                    disk = disk[:m+1] + [(i, dj)] + disk[m+1:]
                    disk[n] = ('.', j2)
                    break      
    disk_list = []
    for i, j in disk:
        for k in range(j):
            disk_list.append(i)
            
    checksum = 0
    for i in range(0,len(disk_list)):
        try:
            checksum += i*int(disk_list[i])
        except:
            pass
        
    print(f'The filesystem checksum is: {checksum}')