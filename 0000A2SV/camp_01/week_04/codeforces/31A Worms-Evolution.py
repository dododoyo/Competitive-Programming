n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
  for j in range(n):
    for k in range(n):
      if arr[i] + arr[j] == arr[k] and i != j and j != k and i != k:
        print(k+1,j+1,i+1)
        exit(0)
print(-1)