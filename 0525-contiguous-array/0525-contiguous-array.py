class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0: nums[i] = -1
        prefix_sum = [nums[0]]*(len(nums))
        for i in range(1,len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]
            
        last_seen = {}
        longest_sub = 0
        
        for i in range(len(prefix_sum)):
            if prefix_sum[i] == 0:
                if i > 0:
                    longest_sub = max(i+1,longest_sub)
            else:
                if prefix_sum[i] in last_seen:
                    longest_sub = max(i - last_seen[prefix_sum[i]],longest_sub)
                else:
                    last_seen[prefix_sum[i]] = i
                    
        return longest_sub
        