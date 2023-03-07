class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        #use the array itself to register the frequency of each array
        size = len(nums)
        solution = []
        for i in range(size):
            if(nums[abs(nums[i])-1] < 0):
                solution.append(abs(nums[i]))
            nums[abs(nums[i])-1] *= -1
            
        return solution