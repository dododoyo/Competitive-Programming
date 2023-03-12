class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #iterate through array and modify it
        nums_size = len(nums)
        solution = []
        
        for i in nums:
            nums[i%nums_size -1] += nums_size
        for i in range(nums_size):
            if(nums[i] < nums_size + 1):
                solution.append(i+1)
        return solution
                
            