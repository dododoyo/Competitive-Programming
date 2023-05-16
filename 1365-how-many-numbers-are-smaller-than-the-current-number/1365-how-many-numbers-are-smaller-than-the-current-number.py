class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        all_nums = [0]*101
        for i in nums:
            all_nums[i] +=1
        for i in range(1,101):
            all_nums[i] = all_nums[i]+all_nums[i-1]
        solution = [0]*len(nums)
        
        for i in range(len(nums)):
            if nums[i] == 0:solution[i] = 0
            else:
                solution[i] = all_nums[nums[i]-1]
        return solution