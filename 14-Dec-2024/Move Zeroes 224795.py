# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        holder = 0

        for seeker in range(1,n):
            if nums[seeker] != 0 and nums[holder] == 0:
                nums[seeker],nums[holder] = nums[holder],nums[seeker]
            
            if nums[holder] != 0:
                holder += 1

        return holder