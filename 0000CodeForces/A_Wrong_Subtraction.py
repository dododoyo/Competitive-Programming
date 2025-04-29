from sys import stdin
def i(): return stdin.readline().strip()
def ls(): return [int(x) for x in i().split()]

n, k = ls()

while k:
  if n % 10 == 0:
    n //= 10
  else:
    n -= 1
  k -= 1

print(n)