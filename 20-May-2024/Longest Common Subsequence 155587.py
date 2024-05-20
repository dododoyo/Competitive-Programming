# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m,n = len(s1),len(s2)
        dp = [[0]*(n + 1) for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if s1[row - 1] == s2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
        return dp[m][n]