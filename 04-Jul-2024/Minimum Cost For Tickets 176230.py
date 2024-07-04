# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0 for i in range(days[-1]+1)]

        dy = set(days)
        for i in range(days[-1]+1):
            if i not in dy: 
                dp[i] = dp[i-1]
            else: 
                one_day = dp[max(0,i-1)]
                seven_day = dp[max(0,i-7)]
                selasa_day = dp[max(0,i-30)]

                dp[i]=min( one_day + costs[0], seven_day + costs[1], selasa_day + costs[2])

        return dp[-1]
        