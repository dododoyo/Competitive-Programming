from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charfreq = defaultdict(int)
        for i in s:
            charfreq[i] += 1
        for j in charfreq:
            if (charfreq[j] == 1):
                return s.index(j)
        return -1
        