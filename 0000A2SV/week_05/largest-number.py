class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):    
                str1  = str(nums[j]) + str(nums[j+1])   
                str2  = str(nums[j+1]) + str(nums[j]) 
                if str1 < str2:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        str_arr = [str(i) for i in nums]
        return "".join(str_arr)