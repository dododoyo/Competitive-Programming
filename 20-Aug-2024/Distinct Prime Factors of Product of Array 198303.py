# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        solution = set()
        
        for i in range(len(nums)):
            d = 2
            while d * d <= nums[i]:
                while nums[i] % d == 0:
                    solution.add(d)
                    nums[i] //= d
                d += 1
            if nums[i] != 1:
                solution.add(nums[i])
        
        return len(solution)