from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

for _ in range(ls()[0]):
  n = ls()[0]
  s = inp()

  distinct_till = [1]*n
  distinct_after = [1]*n

  distinct = set()

  for i in range(n):
    distinct.add(s[i])
    distinct_till[i] = len(distinct)

  distinct = set()
  for i in range(n-1,-1,-1):
    distinct.add(s[i])
    distinct_after[i] = len(distinct)

  solution = 0

  for i in range(n-1):
    solution = max(solution,distinct_after[i+1] + distinct_till[i])

  print(solution)
