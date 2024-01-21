def count_subarrays(n, a):
    left, right = 0, 0
    subarrays = []
    while right < n:
        if a[right] > 0:
            if any(x < 0 for x in a[left:right]):
                subarrays.append(a[left:right])
            left = right
        right += 1
    total = sum([abs(i) for i in a])
    if any(x < 0 for x in a[left:right]):
        subarrays.append(a[left:right])
    return total,len(subarrays)
      

for _ in range(int(input())):
  n = int(input())
  a = [int(i) for i in input().split()]

  # return maximum possible sum
  # minimum number of operations to get this sum.
  # operation is to change l-r to -1*(l-r)

  # return the number of subaays only
  # containing only non-positive integers
  print(*count_subarrays(n,a))
