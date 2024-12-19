class Coordinate:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance
        
def valid(x, y):
    return x >= 0 and x < GRID_SIZE+1 and y >= 0 and y < GRID_SIZE+1

FALLEN_BYTES = 2084
GRID_SIZE = 70

with open('Day-18/input.txt') as f:
    lines = f.read().splitlines()
    corrupted_coordinates = []
    n = 0
    for line in lines:
        if n == FALLEN_BYTES:
            break
        x, y = line.split(',')
        corrupted_coordinates.append((int(x), int(y)))
        n += 1
        
start = Coordinate(0, 0, 0)
end = (GRID_SIZE, GRID_SIZE)
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = set()
visited.add((start.x, start.y))

queue = [start]

while len(queue) > 0:
    current = queue.pop(0)
    if (current.x, current.y) == end:
        print(f'The shortest path is {current.distance} steps long.')
        break
    for move in moves:
        new_x = current.x + move[0]
        new_y = current.y + move[1]
        new_distance = current.distance + 1
        if (new_x, new_y) in corrupted_coordinates or not valid(new_x, new_y) or (new_x, new_y) in visited:
            continue
        new_coordinate = Coordinate(new_x, new_y, new_distance)
        if (new_x, new_y) not in visited:
            visited.add((new_x, new_y))
            queue.append(new_coordinate)