# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        n = len(coins)
        # dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
        prev_row = [float('inf') for _ in range(amount+1)] 

        for remain_coin in range(amount+1):
                if remain_coin%coins[0] == 0:
                    prev_row[remain_coin] = remain_coin//coins[0]
        curr_row = prev_row[:]

        for index in range(1,n):
            for remain_coin in range(amount+1):
                take = float('inf')
                not_take = 0 + prev_row[remain_coin]

                if coins[index] <= remain_coin:
                    new_remain_coin = remain_coin-coins[index]
                    # don't move to the next coin because we can take 
                    # the current coin repeatedly
                    take = 1 + curr_row[new_remain_coin]

                curr_row[remain_coin] = min(take,not_take)
            prev_row = curr_row[:]
        

        solution = prev_row[amount]

        if solution == float('inf'):
            return -1
        else:
            return solution
            