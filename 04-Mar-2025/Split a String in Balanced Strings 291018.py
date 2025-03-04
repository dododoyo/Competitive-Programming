# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        score = 0
        left_count = 0
        right_count = 0

        n = len(s)

        for i in range(n):
            if s[i] == "L":
                left_count += 1
            else:
                right_count += 1

            if left_count == right_count:
                score += 1

        return score
        