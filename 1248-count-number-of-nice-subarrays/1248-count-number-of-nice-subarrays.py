from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for index in range(len(nums)):
            if nums[index] % 2 == 0:nums[index] = 0;
            else:nums[index] = 1;
        prefix_map = defaultdict(int)
        current_sum,nice_count = 0,0
        for r in nums:
            current_sum += r
            if current_sum == k:nice_count += 1;
            if (current_sum-k) in prefix_map:
                nice_count += prefix_map[current_sum-k]
            prefix_map[current_sum] += 1
        return nice_count
            
                
            