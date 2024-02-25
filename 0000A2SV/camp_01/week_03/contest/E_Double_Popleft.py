# first two leftmost elements 
# which ever greatest to the left
from collections import deque

n,q = map(int,input().split())
a = list(map(int,input().split()))
max_index = 0
found_pattern = False
max_value = max(a)
early_solutions, dq = {}, deque(a)

for query in range(n):
    dq_0,dq_1 = dq[0],dq[1]
    early_solutions[query+1] = [dq_0,dq_1]
    max_ , min_= max(dq_0,dq_1) , min(dq_0,dq_1)

    if dq_0 == max_value and not found_pattern:
      new_a = list(dq)[1:]
      max_index = query
      found_pattern = True

    first = dq.popleft()
    second = dq.popleft()

    dq.appendleft(max_)
    dq.append(min_)

      
# print(new_a)
for _ in range(q):
  query = int(input())
  if query <= n:
    print(*early_solutions[query])
  else:
    print(a[max_index],new_a[(query-max_index-1)%(n-1)])


