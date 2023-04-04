from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_each = defaultdict(int)
        for i in nums:
            freq_each[i] += 1
        for i in freq_each:
            if freq_each[i] == 1:
                return i