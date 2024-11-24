# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy 

        maximum_profit,minimum_price = 0,prices[0]

        # each price has possibility of being selling point or buying point 
        for price in prices:
            minimum_price = min(minimum_price,price)
            maximum_profit = max(maximum_profit,price-minimum_price)

        return maximum_profit