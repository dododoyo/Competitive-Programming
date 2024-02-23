class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # there is a pattern to the solutions 
        # we can't do it in bruteforce
        MOD = 10**9 + 7
        evens = pow(5,n//2+n%2,MOD) 
        primes = pow(4,n//2,MOD)
        solution = primes*evens
        return solution%MOD