class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        #bruteforce solution
        minimum_sum = 5000
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]<nums[j] and nums[k] < nums[j]:
                        minimum_sum = min(minimum_sum,(nums[i]+nums[j]+nums[k]))
        return -1 if minimum_sum == 5000 else minimum_sum
                    
        