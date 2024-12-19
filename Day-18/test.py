from collections import deque

GRID_SIZE = 70
FALLEN_BYTES = 1940

class Coordinate:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance
        
def valid(x, y):
    return x >= 0 and x < GRID_SIZE+1 and y >= 0 and y < GRID_SIZE+1

def one_path(corrupted_coordinates):
    start = Coordinate(0, 0, 0)
    end = (GRID_SIZE, GRID_SIZE)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    visited.add((start.x, start.y))

    queue = deque([start])

    while len(queue) > 0:
        current = queue.popleft()
        if (current.x, current.y) == end:
            return visited
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
    return set()

with open('Day-18/input.txt') as f:
    lines = f.read().splitlines()
    corrupted_coordinates = set()
    for line in lines:
        x, y = line.split(',')
        corrupted_coordinates.add((int(x), int(y)))
    
    for i in range(FALLEN_BYTES, len(corrupted_coordinates) + 1):
        corrupted_coordinates_iter = list(corrupted_coordinates)[:i]
        path = one_path(corrupted_coordinates_iter)
        if path == set():
            print(f'The first coordinate that breaks the path is: {corrupted_coordinates_iter[-1][0]},{corrupted_coordinates_iter[-1][1]}')
            break