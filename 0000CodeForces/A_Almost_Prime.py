from collections import defaultdict
def isAlmostPrime(i):
  factors,d = defaultdict(int),2
  while d*d <= i:
    while i%d == 0:
      factors[d] += 1
      i //= d
    d += 1
  if i > 1:
    factors[i] += 1
  return len(factors) == 1

def prime_seive(n):
  is_prime = [True for _ in range(n+1)]
  is_prime[0] = is_prime[1] = False
  i = 2
  root = int(n**0.5)
  while i <= root:
    if is_prime[i]:
      j = i*i
      for k in range(j,n+1,i):
        is_prime[j] = False
    i += 1
  return is_prime

def gcd(a,b):
  while b != 0:
      a, b = b, a % b
  return a


# n = int(input())
# almost_primes = 0
# for i in range(1,n+1):
#   almost_primes += isAlmostPrime(i)
# print(almost_primes)
  
print(prime_seive(7))
