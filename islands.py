from util import Queue, Stack

islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

def island_counter(matrix):
    #walk through each cell of matrix
    #count up connected components
    visited = []
    island_count = 0
    for i in range(len(matrix)): #find height
        visited.append([False] * len(matrix[0])) #find width

    #walk-through
    for col in range(len(matrix[0])): #length
        for row in range(len(matrix)): #width
            #reaching a 1
            if not visited[row][col]: #first value height, second value width, because of set-up
                if matrix[row][col] == 1:
                    visited = dft(col, y, matrix, visited)
                    island_count += 1
                else:
                     visited[row][col] = True

def dft(col, row, matrix, visited):
    s = Stack()
    s.push((col, row))
    while s.size > 0:
        v = s.pop
        col= v[0]
        row = v[1]

        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors((x, y), matrix):
                s.push(neighbor)
    return visited