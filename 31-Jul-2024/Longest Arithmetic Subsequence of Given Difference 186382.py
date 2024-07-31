# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for i in arr:
            x = i - difference
            if x in dp:
                dp[i] = dp[x] + 1
            else:
                dp[i] = 1
        return max(dp.values())