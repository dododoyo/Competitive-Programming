from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freqs = Counter(arr)
        for key,value in freqs.items():
            if value > len(arr)/4:
                return key


        