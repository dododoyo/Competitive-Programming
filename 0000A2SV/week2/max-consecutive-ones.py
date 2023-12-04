class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left,right = 0,0
        maximum_consecutive_ones = 0
        while right < len(nums):
            while  right < len(nums) and nums[right] == 1:
                right += 1
            maximum_consecutive_ones = max(maximum_consecutive_ones,right-left);
            right += 1
            left = right
        return maximum_consecutive_ones


        