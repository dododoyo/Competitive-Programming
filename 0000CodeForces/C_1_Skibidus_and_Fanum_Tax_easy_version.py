from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

for _ in range(ls()[0]):
    n,m = ls()
    a = ls()
    b = ls()[0]

    current = -float('inf')
    can_sort = True
    for x in a:
        mn, mx = min(x, b - x), max(x, b - x)
        if mn >= current:
            current = mn
        elif mx >= current:
            current = mx
        else:
            can_sort = False
            break
        
    print("YES" if can_sort else "NO")



# for _ in range(ls()[0]):
#   n,m = ls()
#   a = ls()
#   b = ls()[0]

#   possible = []

#   for i in range(n):
#       vals = sorted([a[i], b - a[i]])
#       possible.append(vals)
  
#   can_sort = True

#   prev = float('-inf')
#   for i in range(n):
#       found = False

#       for val in possible[i]:
#           if val >= prev:
#               prev = val
#               found = True
#               break
          
#       if not found:
#           can_sort = False
#           break
  
#   print("YES" if can_sort else "NO")

