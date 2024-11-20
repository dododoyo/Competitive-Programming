# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        len1,len2 = len(s1),len(s2)

        prev_memo = [0 for i in range(len2+1)]
        current_memo = [0 for i in range(len2+1)]

        for index1 in range(1,len1+1):
            current_memo = [0 for i in range(len2+1)]
            for index2 in range(1,len2+1):
                if s1[index1-1] == s2[index2-1]:
                    current_memo[index2] = 1 + prev_memo[index2-1]
                else:
                    current_memo[index2] = max(current_memo[index2-1],prev_memo[index2])    
            prev_memo = current_memo[:]
        return prev_memo[len2]

