# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def sum_of_prime_factors(self,n):
        factors_sum = 0
        for i in range(2, n+1):
            while n % i == 0:
                factors_sum += i
                n //= i

        return factors_sum
        
    def smallestValue(self, n: int) -> int:
        while True:
            new_n = self.sum_of_prime_factors(n)

            if n == new_n:
                break
            n = new_n

        return n
