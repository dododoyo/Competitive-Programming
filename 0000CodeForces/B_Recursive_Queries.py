from bisect import bisect_left,bisect_right
def f(x):
  solution = 1

  while x:
    if x%10 != 0:
      solution *= x%10
    x //= 10

  return solution

def g(x):
  if x < 10:
    return x
  
  return g(f(x))

valids = [[] for i in range(10)]
for i in range(1, 10 ** 6 + 1):
    valids[g(i)].append(i)


for _ in range([int(i) for i in input().split()][0]):
  left,right,target = [int(i) for i in input().split()]

  print(valids[target])
  
  count = bisect_right(valids[target], right) - bisect_left(valids[target], left)

  print(count)