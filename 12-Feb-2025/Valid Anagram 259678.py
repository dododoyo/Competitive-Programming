# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0]*26
        OFFSET = ord('a')

        for c in s:freq[ord(c)-OFFSET] += 1
        for c in t:freq[ord(c)-OFFSET] -= 1

        for i in freq:
            if i != 0:
                return False

        return True