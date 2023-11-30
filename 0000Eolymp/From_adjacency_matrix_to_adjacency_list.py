n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

adj_list = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] == 1:
            adj_list[i].append(j+1)

for i in range(n):
    print(len(adj_list[i]),end=' ')
    for j in adj_list[i]:
        print(j,end=' ')
    print()