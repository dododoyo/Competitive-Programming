# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstPointer = 0
        secondPointer = 1
        maxProfit = 0
        
        while(secondPointer < len(prices)):        
            if(prices[secondPointer] > prices[firstPointer]):
                if(prices[secondPointer] - prices[firstPointer] > maxProfit):
                    maxProfit = prices[secondPointer] - prices[firstPointer]
                secondPointer += 1
            else:
                firstPointer = secondPointer
                secondPointer += 1
                
        return maxProfit