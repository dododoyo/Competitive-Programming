class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        holder = 0
        for seeker in range(len(nums)):
            if nums[seeker] != val and nums[holder] == val:
                nums[holder],nums[seeker] = nums[seeker],nums[holder]
            print(nums[holder] != val)
            if nums[holder] != val:
                holder += 1
        return holder 
        