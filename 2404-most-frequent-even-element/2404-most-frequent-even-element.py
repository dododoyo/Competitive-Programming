from collections import defaultdict
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        #maxes holds most frequent number(maxes[1]) and it's frequency(maxes[0])
        maxes = [0,-1]
        for i in nums:
            if i%2 == 0:
                freq[i] += 1
                if maxes[0] < freq[i]:
                    maxes[0] = freq[i]
                    maxes[1] = i
                elif maxes[0] == freq[i]:
                    maxes[1] = min(i,maxes[1])
                
        return maxes[1]