class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        right,solution = 0,float('inf')
        nums.sort()
        for right in range(len(nums)-2):
            min_diff = self.searchPair(target - nums[right],nums,right+1)
            if  abs(target-(min_diff+nums[right])) <  abs(target-solution):
                solution = min_diff+nums[right]
        return solution
        
    def searchPair(self,target,nums,start):
        left,right,solution = start,len(nums)-1,float('inf')
        while left < right:
            # update the minimum distanced solution based on our condition
            if abs(target-(nums[right]+nums[left])) < abs(target - solution):
                solution = nums[right] + nums[left]
            # update the pointers on the numbers based on value of sum 
            if nums[right] + nums[left] > target:right -= 1
            elif nums[right] + nums[left] < target:left += 1
            else:return target
        return solution
