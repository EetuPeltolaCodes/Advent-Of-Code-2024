BLINKS = 25

with open('Day-11\input.txt') as f:
    data = f.read().split(' ')
    data = [int(i) for i in data]
    for i in range(1,BLINKS+1):
        new_arrangement = []
        for node in data:
            if node == 0:
                new_arrangement.append(1)
            elif len(str(node)) % 2 == 0:
                half = len(str(node)) // 2
                new_arrangement.append(int(str(node)[:half]))
                new_arrangement.append(int(str(node)[half:]))
            else:
                new_arrangement.append(node*2024)
        data = new_arrangement
    print(f'There are {len(data)} stones after {BLINKS} blinks')