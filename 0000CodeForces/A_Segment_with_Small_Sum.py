n,s = map(int,input().split())
a = [int(i) for i in input().split()]
summ,solution = 0,0
left = 0
for right in range(len(a)):
  summ += a[right]
  while summ >= s:
    summ -= a[left]
    left += 1
  solution = max(solution,right-left+1)
print(solution)
