class Solution:
    def swapElements(self,nums:List[int],swapped:int,end) -> List[int]:
        holder = 0
        for seeker in range(end):
            # if the number seeked is not the one to be at end 
            # and if the number held is the one to be at the end
            # swap the elements
            if nums[seeker] != swapped and nums[holder] == swapped:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
            if nums[holder] != swapped:
                holder += 1
        return nums,holder
    def sortColors(self, nums: List[int]) -> None:
        nums,end = self.swapElements(nums,2,len(nums))
        nums,end = self.swapElements(nums,1,end)
        return nums


        