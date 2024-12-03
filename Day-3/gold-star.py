import re

with open('Day-3\input.txt') as file:
    data = file.read()
 
dos = re.split(r'do\(\)',data)
correct_inputs = []
for x in dos:
    dont = re.search(r'don\'t\(\)', x)
    if dont == None:
        correct_inputs.append(re.findall(r'mul\((\d+),(\d+)\)', x))
    else:
        correct_inputs.append(re.findall(r'mul\((\d+),(\d+)\)', x[:dont.start()]))
        
answer = 0 
for correct_input in correct_inputs:
    answer += sum([int(x)*int(y) for x, y in correct_input])
            
print(f'The Sum of the multiplication of the two numbers is: {answer}')