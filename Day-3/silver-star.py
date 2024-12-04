import re

with open('Day-3\input.txt') as file:
    data = file.read()
    
correct_inputs = re.findall(r'mul\((\d+),(\d+)\)', data)
answer = sum([int(x)*int(y) for x, y in correct_inputs])

print(f'The Sum of the multiplication of the two numbers is: {answer}') 