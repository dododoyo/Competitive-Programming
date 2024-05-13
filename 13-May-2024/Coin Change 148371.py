# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        min_coin_for_coin = [0]*(amount+1)

        for i in range(1,amount+1):
            min_coin_for_coin[i] = float('inf')
            for coin in coins:
                if (coin <= i and (min_coin_for_coin[i-coin] != float('inf'))):
                    min_coin_for_coin[i] = min(min_coin_for_coin[i],1+min_coin_for_coin[i-coin])
        if min_coin_for_coin[amount] == float('inf'):
            return -1
        else:
            return min_coin_for_coin[amount]