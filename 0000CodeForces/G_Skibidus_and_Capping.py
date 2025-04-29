from math import lcm
from sys import stdin
from collections import defaultdict

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]

def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

def generate_semis(primes, max_val):
    semi_primes = set()
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            semi_prime = primes[i] * primes[j]
            if semi_prime > max_val:
                break
            semi_primes.add(semi_prime)
    return semi_primes


def count_semis(a, semi_primes):
    freq = defaultdict(int)
    for num in a:
        freq[num] += 1
    
    count = 0
    unique_nums = list(freq.keys())
    
    for i in range(len(unique_nums)):
        for j in range(i, len(unique_nums)):
            lcm_val = lcm(unique_nums[i], unique_nums[j])
            if lcm_val in semi_primes:
                if i == j:
                    count += freq[unique_nums[i]] * (freq[unique_nums[i]] + 1) // 2
                else:
                    count += freq[unique_nums[i]] * freq[unique_nums[j]]
    return count

MAX_N = 2 * (10**5)
primes = sieve(MAX_N)
semi_primes = generate_semis(primes, MAX_N)

for _ in range(ls()[0]):
    n = ls()[0]
    a = ls()
    print(count_semis(a, semi_primes))