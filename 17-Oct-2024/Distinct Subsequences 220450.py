# Problem: Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = defaultdict(lambda : -1)

        def get_distinct(s_pointer,t_pointer):
            if t_pointer == len(t):
                return 1
            if s_pointer == len(s):
                return 0
            pick = 0
            if s[s_pointer] == t[t_pointer]:
                if dp[s_pointer+1,t_pointer+1] == -1:
                    pick = get_distinct(s_pointer+1,t_pointer+1) 
                else:
                    pick =  dp[s_pointer+1,t_pointer+1]

            if dp[s_pointer+1,t_pointer] == -1:
                not_pick = get_distinct(s_pointer+1,t_pointer) 
            else:
                not_pick =  dp[s_pointer+1,t_pointer]

            dp[s_pointer,t_pointer] = pick+not_pick
            return dp[s_pointer,t_pointer]

        return get_distinct(0,0)