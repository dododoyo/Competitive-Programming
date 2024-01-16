n,k = map(int,input().split())
number = 0
if n%2:
  # if n is odd
  if k > n//2+1 :
    # access evens
    number = 2*((k-n//2)-1)
  else:
    number = 2*(k-1) + 1
else:
  # if n is even
  if k > (n//2) :
    # access evens
    number = 2*((k-n//2))
  else:
    number = 2*(k-1) + 1
print(number)
