from collections import deque
n,m = map(int,input().split())
line_up = list(map(int,input().split()))
#create new list of elements with their indeces
for i in range(n):
    line_up[i] = [i+1,line_up[i]]
line_up = deque(line_up)

while len(line_up) > 1:
        popped = line_up.popleft()
        if popped[1] > m:
            popped[1] -= m
            line_up.append(popped)

print(line_up[0][0])