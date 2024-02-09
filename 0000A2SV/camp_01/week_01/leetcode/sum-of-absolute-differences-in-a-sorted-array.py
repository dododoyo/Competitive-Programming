class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # when solving for each element we see that it 
        # can be simplified to a mathematical equation given as 
        #solution[i] = n[i]*(2*i -n +1) - suffix_till_i + prefix_after_i
        n = len(nums)
        forward_prefix = [nums[0]]*n
        backward_prefix = [nums[-1]]*n
        for i in range(1,n):
            forward_prefix[i] = forward_prefix[i-1] + nums[i]
            backward_prefix[n-i-1] = backward_prefix[n-i] + nums[n-i-1]
        # using the mathematical formula we can create our solution 
        solution = [0]*n
        for i in range(n):
            if i == 0:
                solution[i] = backward_prefix[i+1] - (n-1)*nums[i]
            elif i == n-1:
                solution[i] = (n-1)*nums[i] - forward_prefix[i-1]
            else:
                solution[i] = nums[i]*(2*i -n + 1) + backward_prefix[i+1] - forward_prefix[i-1]
        return solution