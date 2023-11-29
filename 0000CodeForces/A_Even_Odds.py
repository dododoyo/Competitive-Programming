n,k = map(int,input().split())
# n is even 
if n%2 == 0:
    if k > n//2:#means we are asked for even parts
        print(2*(k-n//2))
    else:
        print(2*k-1)
# n is odd
else:
    if k > n//2+1:#means we are asked for even parts
        print(2*(k-n//2-1))
    else:
        print(2*k-1)