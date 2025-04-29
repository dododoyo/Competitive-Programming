from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


n,queries = ls()
worlds_height = ls()

diff_forward = [0]*(n)
diff_backward = [0]*(n)

for i in range(1,n):
  diff_forward[i] = max(0,worlds_height[i-1] - worlds_height[i])

for i in range(n-2,-1,-1):
  diff_backward[i] = max(0,worlds_height[i+1] - worlds_height[i])


forward_prefix = [0]*(n+1)
backward_prefix = [0]*(n+1)

for i in range(n):
  forward_prefix[i+1] = forward_prefix[i] + diff_forward[i]

for i in range(n):
  backward_prefix[i+1] = backward_prefix[i] + diff_backward[i]


for _ in range(queries):
  s,t = ls()
  if s < t:
    print(forward_prefix[t] - forward_prefix[s])
  else:
    print(backward_prefix[s-1] - backward_prefix[t-1])
