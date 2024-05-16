# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price,maximum_profit = prices[0],0
        
        for i in range(1,len(prices)):
            price = prices[i]
            maximum_profit = max(maximum_profit, price - minimum_price)
            minimum_price = min(minimum_price, price)
            
        return maximum_profit