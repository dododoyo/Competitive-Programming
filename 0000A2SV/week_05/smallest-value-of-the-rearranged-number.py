class Solution:
    def smallestNumber(self, nums: int) -> int:
        if nums == 0:
            return 0
        is_neg = nums < 0
        nums = abs(nums)
        nums = list(str(nums))
        if is_neg:
            for i in range(len(nums)-1):
                for j in range(len(nums)-i-1):    
                    str1  = nums[j] + nums[j+1]   
                    str2  = nums[j+1] + nums[j] 
                    if str1 < str2:
                        nums[j],nums[j+1] = nums[j+1],nums[j]
        else:
            for i in range(len(nums)-1):
                for j in range(len(nums)-i-1):    
                    str1  = nums[j] + nums[j+1]   
                    str2  = nums[j+1] + nums[j] 
                    if str1 > str2:
                        nums[j],nums[j+1] = nums[j+1],nums[j]
        i = 0 
        while i < len(nums) and nums[i] == "0":i+=1
        if i != 0:
            nums[i],nums[0] = nums[0],nums[i]
        str_arr = [str(i) for i in nums]
        solution = int("".join(str_arr))
        return -solution if is_neg else solution
        