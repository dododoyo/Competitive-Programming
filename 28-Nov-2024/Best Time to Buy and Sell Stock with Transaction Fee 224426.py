# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit_memo = {}
        n = len(prices)
        BUY, SELL = 0, 1

        profit_memo[(-1,BUY)] = -float('inf')
        profit_memo[(-1,SELL)] = 0


        for i in range(n):
            # buy profit today => you sold yesterday
            buying_profit = -prices[i] + profit_memo[(i-1,SELL)]

            # sell profit today => you bought today 
            selling_profit = (prices[i] + profit_memo[(i-1,BUY)]) - fee

            # fee is deducted when a stock is sold
            profit_memo[i,BUY] = max(buying_profit,profit_memo[i-1,BUY])
            profit_memo[i,SELL] = max(selling_profit,profit_memo[i-1,SELL])

        return profit_memo[(n-1,SELL)]
        