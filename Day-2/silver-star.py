with open("Day-2\input.txt", "r") as file:
    data = file.read().split("\n")

file.close()

safe = 0
for level in data:
    reports = level.split(" ")
    state = 0   # -1 for decreasing, 1 for increasing
    if int(reports[0]) > int(reports[1]):
            state = -1
    elif int(reports[0]) < int(reports[1]):
            state = 1
    for i in range(len(reports)-1):
        diff = abs(int(reports[i]) - int(reports[i+1]))
        if state == 1:
            if int(reports[i]) > int(reports[i+1]):
                break
        elif state == -1:
            if int(reports[i]) < int(reports[i+1]):
                break
        if diff < 1 or diff > 3:
            break
        
        if i == len(reports)-2:
            safe += 1
            
print(f"The number of safe levels is: {safe}")