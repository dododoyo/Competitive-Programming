class Solution:
    def reverse(self, x: int) -> int:
        nums = str(x)
        solution = ""
        if(x<0):
            nums= nums[1:]
            solution = -1*int(nums[::-1])
        else:
            solution = int(nums[::-1])
        
        if(solution <-2147483648 or solution >2147483647):
            return 0
        return solution
        