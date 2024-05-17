# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        HOLD,SELL,COOLDOWN = 0,1,2

        dp,n = {},len(prices)

        dp[-1,HOLD] = -float("inf")
        dp[-1,SELL] = 0
        dp[-1,COOLDOWN] = 0

        for i in range(n):
            # at any day you can either sell a stock , buy a stock or cool down
            stock_price = prices[i]

            # when buying today we can't take yesterday's buying state
            # because before buying it is always cooldown
            buying_profit_today = dp[i-1,COOLDOWN] - stock_price
            dp[i,HOLD] = max(dp[i-1,HOLD],buying_profit_today)

            selling_profit_today = dp[i-1,HOLD] + stock_price
            dp[i,SELL] = max(dp[i-1,SELL],selling_profit_today)

            # if we cool down today the max proft is either (cooling down yesterday 
            # or selling yesterday) we can't get the profit of selling today 
            # because we are cooling down

            dp[i,COOLDOWN] = max(dp[i-1,COOLDOWN],dp[i-1,SELL])
    
        if dp[n-1,SELL] > dp[n-1,COOLDOWN]:
            return dp[n-1,SELL]
        else:
            return dp[n-1,COOLDOWN]