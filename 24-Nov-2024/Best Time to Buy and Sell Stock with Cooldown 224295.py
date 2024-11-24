# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        HOLD,SELL,COOLDOWN = 0,1,2
        n = len(prices)

        # HOLD, SELL, COOLDOWN
        profit_memo = [[-float('inf'),0,0] for i in range(n+1)]

        for i in range(n):
            # hold profit 
            # if you plan to buy today you must've cooldowned yesterday
            holding_profit = -prices[i] + profit_memo[i][COOLDOWN]
            profit_memo[i+1][HOLD] = max(profit_memo[i][HOLD],holding_profit)

            # sell profit
            # if you plan to sell today you must have hold yesterday
            selling_profit = prices[i] + profit_memo[i][HOLD]
            profit_memo[i+1][SELL] = max(profit_memo[i][SELL],selling_profit)

            # cooldown profit 
            # you either sold or cooldown yesterday.
            profit_memo[i+1][COOLDOWN] = max(profit_memo[i][COOLDOWN],profit_memo[i][SELL])

        return max(profit_memo[n][COOLDOWN],profit_memo[n][SELL])
