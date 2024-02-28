class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # circularity can be represented with concantenation 
        n = len(nums)
        solution, stack = [-1]*n, []
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                # if whatever that occured now is greater than 
                # the top it will pop it
                solution[stack.pop()] = nums[i%n]
            if i < n:stack.append(i)
        return solution