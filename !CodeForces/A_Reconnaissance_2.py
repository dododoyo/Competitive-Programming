n = int(input())
circle = list(map(int,input().split()))
min_len = abs(circle[0] - circle[n-1])
neighbours = [1,n]
for i in range(1,n):
    #if you find a new minimum difference
    #make it the new min_len between neighbours
    if abs(circle[i] - circle[i-1])<min_len:
        min_len = abs(circle[i]-circle[i-1])
        neighbours = [i+1,i]
print(neighbours[1],neighbours[0])