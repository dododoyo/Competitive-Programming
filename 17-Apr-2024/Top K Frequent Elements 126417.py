# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_map = [[value,key] for key,value in freq.items()]
        heapq.heapify(freq_map)

        while len(freq_map) > k:
            heapq.heappop(freq_map)

        return [num[1] for num in freq_map]
