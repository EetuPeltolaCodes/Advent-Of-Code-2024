def initial_check(reports, state):
    proposal_removed = []
    for i in range(0,len(reports)-1):
        diff = abs(int(reports[i]) - int(reports[i+1]))
        if state == 1:
            if int(reports[i]) > int(reports[i+1]):
                proposal_removed.append(i)
                proposal_removed.append(i+1)
                proposal_removed.append(i-1)
                return proposal_removed
                
        elif state == -1:
            if int(reports[i]) < int(reports[i+1]):
                proposal_removed.append(i)
                proposal_removed.append(i+1)
                proposal_removed.append(i-1)
                return proposal_removed
        if diff < 1 or diff > 3:
            proposal_removed.append(i)
            proposal_removed.append(i+1)
            proposal_removed.append(i-1)
            return proposal_removed
    
    return proposal_removed

def check(original_reports, removed_index):
    reports = original_reports[:removed_index] + original_reports[removed_index + 1:]
    state = 0   # -1 for decreasing, 1 for increasing
    if int(reports[0]) > int(reports[1]):
        state = -1
    elif int(reports[0]) < int(reports[1]):
        state = 1
    
    for i in range(len(reports)-1):
        diff = abs(int(reports[i]) - int(reports[i+1]))
        if state == 1:
            if int(reports[i]) > int(reports[i+1]):
                return 0
        elif state == -1:
            if int(reports[i]) < int(reports[i+1]):
                return 0
        if diff < 1 or diff > 3:
            return 0
    
    return 1

with open("Day-2\input.txt", "r") as file:
    data = file.read().split("\n")


safe = 0
non_safe1 = []
k=0
for level in data:
    reports = level.split(" ")
    removed_layers = 0
    state = 0   # -1 for decreasing, 1 for increasing
    i = 0
    if int(reports[0]) > int(reports[1]):
        state = -1
    elif int(reports[0]) < int(reports[1]):
        state = 1
        
    removed = initial_check(reports, state)
    
    if removed == []:
        safe += 1
        
    for i in removed:
        n = check(reports, i)
        if n > 0:
            safe += 1
            break
             
            
print(f"The number of safe levels is: {safe}")
