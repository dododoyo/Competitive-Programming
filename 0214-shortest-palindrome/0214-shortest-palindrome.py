class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_s= s[::-1]
        for i in range(len(s)):
            if s.startswith(reversed_s[i:]):
                return reversed_s[:i] + s

        return reversed_s + s