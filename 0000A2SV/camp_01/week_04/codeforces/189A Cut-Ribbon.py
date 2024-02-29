n,a,b,c = map(int,input().split())
# if n is a multiple of a,b,and c we can
# see that n = x*a + y*b + z*c
# so we want to maximize x+y+z

solution = 0
for x in range(0,4001):
  for y in range(0,4001):
    zc = n - x*a - y*b
    if zc < 0:
      break
    if zc % c == 0:
      # if z is an integer it means we 
      # have posssible x, y, and z 's  
      # that satisfy our codition
      solution = max(solution, x+y+(zc//c))

print(solution)
