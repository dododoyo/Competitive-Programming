from collections import defaultdict
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in nums:
            if i%2 == 0:
                freq[i] += 1
        maxes = [0,-1]
        for i in freq:
            if freq[i] > maxes[0]:
                maxes[0] = freq[i]
                maxes[1] = i
            elif freq[i] == maxes[0]:
                maxes[0] = freq[i]
                maxes[1] = min(maxes[1],i)
                
        return maxes[1]