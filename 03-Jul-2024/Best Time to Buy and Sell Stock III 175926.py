# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        left_profit = [0]*n
        right_profit = [0]*n

        min_price = 10**6
        max_profit = -1

        for i in range(n):
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit,prices[i]-min_price)
            left_profit[i] = max_profit

        max_price = -1
        max_profit = -1

        for i in range(n-1,-1,-1):
            max_price = max(max_price,prices[i])
            max_profit = max(max_profit,max_price-prices[i])
            right_profit[i] = max_profit
        
        total_profit = [left_profit[i] + right_profit[i] for i in range(n)]
        
        return max(total_profit)

