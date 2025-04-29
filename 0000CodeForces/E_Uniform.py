from itertools import product
from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

a = input()
b = input()
OFFSET = ord('a')

if len(a) != len(b):
	print (-1)
	exit(0)
	
n = ls()[0]
graph = [[float('inf')] * 26 for _ in range(26)]
for i in range(26): graph[i][i] = 0

for i in range(n):
	# u, v, w = input().split()
	u,v,w = ls()
	graph[ord(u)-OFFSET][ord(u)-OFFSET] = min(graph[ord(u)-OFFSET][ord(u)-OFFSET], int(w))

for k, i, j in product(range(26), repeat = 3):
	graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

tot = 0
ans = ''
for x, y in zip(a, b):
	if x == y:
		ans += x
		continue
	
	rx, ry = ord(x)-OFFSET,ord(y)-OFFSET
	best = float('inf')
	sele = -1
	for i in range(26):
		t = graph[rx][i] + graph[ry][i]
		if t < best:
			best = t
			sele = i
			
	if best == float('inf'):
		print (-1)
		exit(0)
		
	tot += best
	ans += chr(sele + 97)

print(tot)
print(ans)
