for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  print("NO") if len(set(arr)) != n else print("YES")