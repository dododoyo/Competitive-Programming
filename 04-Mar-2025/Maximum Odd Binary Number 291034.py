# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # put the one "one" to the last to make sure 
        # and make the rest of ones to the left

        n = len(s)
        ones = 0

        for i in range(n):
            ones += (s[i] == "1")

        return "1"*(ones-1) + "0"*(n-ones) + "1"
        