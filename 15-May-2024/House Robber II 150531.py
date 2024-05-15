# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def find_robbed(self,nums,n):
        one_prev,two_prev = max(nums[0],nums[1]),nums[0]
        
        for i in range(2,n-1):
            pick = nums[i] + two_prev
            not_pick = one_prev

            two_prev = one_prev
            one_prev = max(pick,not_pick)

        return one_prev

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)
        else:
            # first and last can't be together.
            first_subarray = self.find_robbed(nums[:n-1],n)
            second_subarray = self.find_robbed(nums[1:n],n)
            return max(second_subarray,first_subarray)
        
        