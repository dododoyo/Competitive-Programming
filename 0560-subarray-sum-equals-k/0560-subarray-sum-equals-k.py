from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_count,current_sum = 0,0;
        prefix_map = defaultdict(int);
        prefix_map[0] = 1;
        for i in nums:
            current_sum += i
            if current_sum-k in prefix_map:
                subarray_count += prefix_map[current_sum-k]
            prefix_map[current_sum] += 1
        return subarray_count
            