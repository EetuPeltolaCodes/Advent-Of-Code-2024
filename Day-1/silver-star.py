import numpy as np

with open("Day-1\input.txt", "r") as file:
    data = file.read().split("\n")
    list1 = []
    list2 = []
    for i in data:
        element = i.split(" ")
        list1.append(int(element[0]))
        list2.append(int(element[-1]))
        
file.close()
    
sorted_list1 = np.array(sorted(list1))
sorted_list2 = np.array(sorted(list2))

distance = np.sum([abs(sorted_list1-sorted_list2)], axis=1)[0]
print(f"The sum of the distances between the two lists is: {distance}")