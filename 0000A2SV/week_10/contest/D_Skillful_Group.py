n = int(input())
arr = [int(i) for i in input().split()]

distinct = len(set(arr))

if distinct == n:
  print(0)
  exit(0)

to_be_removed = n - distinct

# find the minimum size of subarray 
# with exactly to be removed numbers


