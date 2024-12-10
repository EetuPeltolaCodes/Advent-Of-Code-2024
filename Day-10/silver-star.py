with open('Day-10/input.txt', 'r') as f:
    data = f.read().splitlines()
    matrix = [list(row) for row in data]
    trailheads = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            matrix[i][j] = int(matrix[i][j])
            if matrix[i][j] == 0:
                trailheads.append((i, j))
    boundary_x = i
    boundary_y = j
    score = 0
    for i,j in trailheads:
        n = 1
        neighbors = set()
        if i-1 >= 0:
            if matrix[i-1][j] == 1:
                neighbors.add((i-1, j))
        if i+1 <= boundary_x:
            if matrix[i+1][j] == 1:
                neighbors.add((i+1, j))
        if j-1 >= 0:
            if matrix[i][j-1] == 1:
                neighbors.add((i, j-1))
        if j+1 <= boundary_y:
            if matrix[i][j+1] == 1:
                neighbors.add((i, j+1))
        while neighbors:
            n += 1
            new_neighbors = set()
            for i, j in neighbors:
                if i-1 >= 0:
                    if matrix[i-1][j] == n:
                        new_neighbors.add((i-1, j))
                if i+1 <= boundary_x:
                    if matrix[i+1][j] == n:
                        new_neighbors.add((i+1, j))
                if j-1 >= 0:
                    if matrix[i][j-1] == n:
                        new_neighbors.add((i, j-1))
                if j+1 <= boundary_y:
                    if matrix[i][j+1] == n:
                        new_neighbors.add((i, j+1))
            neighbors = new_neighbors
            if n == 9:
                score += len(neighbors)
    
    print(f'The sum of scores from all trailheads is {score}')