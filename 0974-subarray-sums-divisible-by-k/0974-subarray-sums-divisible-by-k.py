from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map,current_sum = defaultdict(int),0
        for number in nums:
            current_sum +=  number 
            prefix_map[current_sum%k] += 1
        subarray_count = prefix_map[0]
        for item,each_freq in prefix_map.items():
            subarray_count += (each_freq*(each_freq-1))//2 
        return subarray_count
            
        