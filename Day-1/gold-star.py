with open("Day-1\input.txt", "r") as file:
    data = file.read().split("\n")
    list1 = []
    list2 = []
    for i in data:
        element = i.split(" ")
        list1.append(int(element[0]))
        list2.append(int(element[-1]))
    
    file.close()

total_similarity_score = 0
for node in list1:
    appearances = 0
    for node2 in list2:
        if node == node2:
            appearances += 1
    total_similarity_score += node * appearances
    
print(f"The total similarity score is: {total_similarity_score}")