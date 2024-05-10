# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    stairs_map = [-1]*46

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n  

        one_before = self.stairs_map[n-1] if self.stairs_map[n-1] != -1 else self.climbStairs(n-1)
        two_before = self.stairs_map[n-2] if self.stairs_map[n-2] != -1 else self.climbStairs(n-2)

        self.stairs_map[n] = (one_before + two_before)
        
        return self.stairs_map[n]