from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        eachFreq = defaultdict(int);
        for i in nums:
            eachFreq[i] += 1
        for i in eachFreq:
            if eachFreq[i] == 1:
                return i;
        