# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder,seeker = 0,1
        n = len(nums)

        while seeker < n:
            while seeker < n and nums[holder] == nums[seeker]:
                seeker += 1
            else:
                if seeker < n:
                    holder += 1
                    nums[holder] = nums[seeker]
            seeker += 1

        return holder + 1