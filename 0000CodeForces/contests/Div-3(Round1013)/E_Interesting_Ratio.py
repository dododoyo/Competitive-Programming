t = int(input())

def primes(n):
    if n < 2:
        return []

    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    p = 2
    while p * p <= n:
        if isPrime[p]:
            for i in range(p * p, n + 1, p):
                isPrime[i] = False
        p += 1

    return [num for num, prime in enumerate(isPrime) if prime]

for _ in range(t):
    n = int(input())
    p = primes(n)
    solution = 0
    for prime in p:
        solution += n // prime
    print(solution)