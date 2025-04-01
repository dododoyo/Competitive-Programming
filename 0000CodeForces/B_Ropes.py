from sys import stdin
def input(): return stdin.readline().strip()

n,k = [int(i) for i in input().split()]
ropes = []
for _ in range(n):
  ropes.append([int(i) for i in input().split()][0])

def valid(cut_length):
  ropes_count = 0
  for rope_length in ropes:
    ropes_count += rope_length//cut_length
  return ropes_count >= k 

diff = 1e-6
low,high = 0,2*max(ropes)
solution = low

while low <= high:
  middle = low + (high-low)/2
  if valid(middle):
    solution = middle 
    low = middle + diff
  else:
    high = middle - diff

print(solution)