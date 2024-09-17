# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        dick = [-1 for _ in range(32)]
        result, mask = 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ vowels[c]
            if dick[mask] != -1 or mask == 0:
                result = max(result, i - dick[mask])
            else:
                dick[mask] = i
        return result
