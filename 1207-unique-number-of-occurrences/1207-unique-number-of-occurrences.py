from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_each = defaultdict(int)
        for i in arr:
            freq_each[i] += 1
        freq = list(freq_each.values())
        freq.sort()
        for i in range(len(freq)-1):
            if freq[i] == freq[i+1]:
                return False
        return True