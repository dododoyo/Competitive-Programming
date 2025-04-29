import sys
from sys import stdin
def input(): return stdin.readline().strip()


sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = [int(i) for i in input().split()]
k = [int(i) for i in input().split()][0]
trees = [int(i) for i in input().split()]

fire_time = [[-1] * (m + 1) for _ in range(n + 1)]
current_level = []

for i in range(k):
    x = trees[2 * i]
    y = trees[2 * i + 1]
    fire_time[x][y] = 0
    current_level.append((x, y))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while current_level:
    next_level = []

    for node in current_level:
        x,y=node
        
        for dx, dy in directions:
            nx,ny= x + dx, y + dy

            if 0 < nx <= n and 0 < ny <= m:
                # not burned
                if fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    next_level.append((nx, ny))

    current_level = next_level[:]

max_fire_time = -1
result_x, result_y = 1, 1 

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if fire_time[i][j] > max_fire_time:
            max_fire_time = fire_time[i][j]
            result_x, result_y = i, j

sys.stdout.write(f"{result_x} {result_y}\n")
