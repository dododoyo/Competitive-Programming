from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

n = ls()[0]
arr = ls()

solution = float('inf')
for i in range(n):
  solution = min(solution,abs(arr[i]))

print(solution)