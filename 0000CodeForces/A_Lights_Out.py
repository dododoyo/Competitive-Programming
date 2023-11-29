def getNeighbours(i_,j_):
    if i_ == 0 and j_ == 0:return [[0,0],[0,1],[1,0]]
    elif i_ == 0 and j_ == 1:return [[0,0],[1,1],[0,2],[0,1]]
    elif i_ == 1 and j_ == 0:return [[0,0],[1,1],[1,0],[2,0]]
    elif i_ == 1 and j_ == 1:return [[2,1],[0,1],[1,0],[1,2],[1,1]]
    elif i_ == 2 and j_ == 0:return [[2,0],[2,1],[1,0]]
    elif i_ == 2 and j_ == 1:return [[1,1],[2,2],[2,1],[2,0]]
    elif i_ == 0 and j_ == 2:return [[0,1],[1,2],[0,2]]
    elif i_ == 1 and j_ == 2:return [[1,1],[0,2],[1,2],[2,2]]
    else:return [[2,2],[2,1],[1,2]]

input_matrix = [[0,0,0],[0,0,0],[0,0,0]]
for k in range(3):
    input_matrix[k] = list(map(int,input().split()))
solution = [[1,1,1],[1,1,1],[1,1,1]]
# get the initial matrix
for i in range(3):
    for j in range(3):
        if input_matrix[i][j]%2 == 1:
            for elmnt in getNeighbours(i,j):
                solution[elmnt[0]][elmnt[1]] = not solution[elmnt[0]][elmnt[1]]
for i in range(3):
    for j in range(3):
        print(int(solution[i][j]),end="")
    print()