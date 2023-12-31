# sliding window

def min_diff(puzzles,n,m):
  puzzles.sort()
  left,right = 0,n-1
  solution = float('inf')
  while right < m:
    solution = min(solution,puzzles[right] - puzzles[left])
    right,left = right+1,left+1
  return solution

n,m = map(int,input().split())
puzzles = [int(i) for i in input().split()]
print(min_diff(puzzles,n,m))