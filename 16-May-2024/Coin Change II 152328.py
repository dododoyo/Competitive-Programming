# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            # for each coin register how many possible ways 
            # they add up to the solution
            
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        
        return dp[amount]