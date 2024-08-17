# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1]*(n+1)
        for number in range(3,n+1):
            current_max = 0
            for j in range(1,number):
                multiple_1 = j * dp[number-j]
                multiple_2 = j * (number-j)
                current_max = max(current_max,multiple_1,multiple_2)
            dp[number] = current_max
        return dp[n]