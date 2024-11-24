# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices) -> int:

        HOLD, SELL = 0, 1
        n = len(prices)
        # buying, selling profit map
        profit_memo = [[-float('inf'),0] for i in range(n+1)]

        for i in range(n):
            selling_profit = prices[i] + profit_memo[i][HOLD]
            buying_profit = -prices[i] + profit_memo[i][SELL]

            # 
            profit_memo[i+1][HOLD] = max(profit_memo[i][HOLD],buying_profit)
            profit_memo[i+1][SELL] = max(profit_memo[i][SELL],selling_profit)


        return profit_memo[n][SELL]