class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        #instead of removing all vals make the first elements valid
        for current_index in range(len(nums)):
            if nums[current_index] != val:
                nums[index] = nums[current_index]
                index += 1
        return index

        