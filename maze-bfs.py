from util import Queue


def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

def printMaze(maze, path=""):
    #enumerate stores things in objects and then returns them as tuples if you list() them
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x
        
        i = start
        j = 0

        pos = set()

        for move in path:
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            pos.add((j, i))

        for j, row in enumerate(maze):
            for i, col in enumerate(row):
                if (j, i) in pos:
                    print("+ ", end="")
                else:
                    print(col + " ", end "")
            print()

def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0

    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False
    return True