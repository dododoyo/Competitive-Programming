# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def withInThreshold(num):
            count = 0
            for number in nums:
                count += ceil(number/num)
            return count <= threshold

        low,high = 1,max(nums)
        solution = high
        while low <= high:
            mid = low + (high-low)//2
            if withInThreshold(mid):
                solution = mid
                high = mid -1
            else:
                low = mid + 1
        return solution

