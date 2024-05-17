# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}
        n = len(prices)
        HOLD_STOCK,SELL_STOCK = 1,0

        dp[-1,HOLD_STOCK] = -float("inf")
        dp[-1,SELL_STOCK] = 0

        for i in range(n):
            stock_price = prices[i]

            hold_profit = dp[i-1,SELL_STOCK] - stock_price
            dp[i,HOLD_STOCK] = max(dp[i-1,HOLD_STOCK],hold_profit)

            sell_profit = dp[i-1,HOLD_STOCK] + stock_price - fee
            dp[i,SELL_STOCK] = max(dp[i-1,SELL_STOCK],sell_profit)

        return dp[n-1,SELL_STOCK]
        