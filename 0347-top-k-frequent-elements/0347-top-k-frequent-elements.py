from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(len(nums) == 1):
            return nums
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        keys = list(freq.keys())
        values = list(freq.values())
        keysAndValues = [0]*len(keys)
        for i in range(len(keys)):
            keysAndValues[i] = [keys[i],values[i]]
        keysAndValues.sort(key = lambda i : i[1],reverse = True)
        solution = [0]*k
        for i in range(k):
            solution[i] = keysAndValues[i][0]
        return solution