# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        pos_map = {} 
        n = len(stones)
        memo = [[-1] * n for _ in range(n)]

        def dp(i, k):
            if i == n - 1:
                return True

            if memo[i][k] != -1:
                return memo[i][k] == 1

            k0, k1, kp = False, False, False

            if stones[i] + k in pos_map:
                k0 = dp(pos_map[stones[i] + k], k)

            if k > 1 and stones[i] + k - 1 in pos_map:
                kp = dp(pos_map[stones[i] + k - 1], k - 1)

            if stones[i] + k + 1 in pos_map:
                k1 = dp(pos_map[stones[i] + k + 1], k + 1)
                
            memo[i][k] = 1 if (k0 or kp or k1) else 0
            return memo[i][k] == 1

        if stones[1] - stones[0] != 1:
            return False

        for i in range(n):
            pos_map[stones[i]] = i

        return dp(1, 1)