class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum,max_sum = sum(nums[:k]),sum(nums[:k])
        for right in range(k,len(nums)):
            current_sum =  current_sum + nums[right] - nums[right-k]
            max_sum = max(max_sum,current_sum)
        return max_sum/k

        