from heapq import heappop,heappush


n,k = map(int,input().split())
arr = [int(num) for num in input().split()]

reverse_prefix = [arr[-1]]*n

for i in range(n-2,-1,-1):
  reverse_prefix[i] = reverse_prefix[i+1] + arr[i]

# print(reverse_prefix)

solution = []

for i in range(1,n):
  heappush(solution,reverse_prefix[i])
  if len(solution) > k-1:
    heappop(solution)


print(sum(solution)+reverse_prefix[0])




