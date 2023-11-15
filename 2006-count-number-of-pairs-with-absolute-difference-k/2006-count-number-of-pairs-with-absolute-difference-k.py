from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        solution = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    solution += 1
        return solution//2
        
        