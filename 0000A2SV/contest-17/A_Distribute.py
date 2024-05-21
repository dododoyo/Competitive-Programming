n = int(input())
arr =[int(num) for num in input().split()]
seen = set()
target = sum(arr)//(n//2)

for i in range(n):
  for j in range(i+1,n):
    if (i not in seen) and (j not in seen) and arr[i] + arr[j] == target:
      seen.add(i)
      seen.add(j)
      print(i+1,j+1)
