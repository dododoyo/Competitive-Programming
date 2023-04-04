class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r,total,solution= 0,0,0,0
        while(r < len(nums)):
            total += nums[r]
            while(nums[r]*(r-l+1) > total+k):
                total -= nums[l]
                l += 1
            solution = max(solution,r-l+1)
            r += 1
        return solution