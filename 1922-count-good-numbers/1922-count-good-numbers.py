class Solution:
     def countGoodNumbers(self, n: int) -> int:
            #there is a pattern in the solutions. . . 
        MOD = 10**9 + 7
        sol, x, i = 5 ** (n % 2),20, n // 2
        while i > 0:
            if i % 2 == 1:sol = (sol * x) % MOD
            x = (x * x) % MOD
            i = i//2
        return sol
    
    