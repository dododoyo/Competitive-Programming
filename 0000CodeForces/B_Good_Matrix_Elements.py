from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


n = ls()[0]
matrix = mt(n)
solution = 0

for r in range(n):
  for c in range(n):
    # add main diagonal 
    if r-c == 0:
      solution += matrix[r][c]

    # add secondary diagonal 
    if abs(r+c) == n-1:
      solution += matrix[r][c]

    # add middle column
    if c == (n-1)//2:
      solution += matrix[r][c]

    # add middle row 
    if r == (n-1)//2:
      solution += matrix[r][c]

# remove repeated 
solution -= 3*matrix[(n-1)//2][(n-1)//2]

print(solution)