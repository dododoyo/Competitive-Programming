# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right=0,0
        total,solution= 0,0

        while(right < len(nums)):
            total += nums[right]
            while(nums[right]*(right-left+1) > total+k):
                total -= nums[left]
                left += 1
            solution = max(solution,right-left+1)
            right += 1
        return solution