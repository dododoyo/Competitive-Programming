class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)-1):
            max_index = i
            for j in range(i+1,len(nums)):
                if(str(nums[j])+str(nums[max_index]) > str(nums[max_index])+str(nums[j])):
                   max_index = j
            nums[i],nums[max_index] = nums[max_index],nums[i]
            
        solution = [str(i) for i in nums]
        return str(int("".join(solution)))
        