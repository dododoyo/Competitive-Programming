from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #return true if all elements occur unique number of times
        freq_dict = defaultdict(int)
        for element in arr:
            freq_dict[element] += 1
        freq = freq_dict.values()
        return len(freq) == len(set(freq))
        