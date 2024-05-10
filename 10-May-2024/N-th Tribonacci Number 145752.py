# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    tri_map = [-1]*40
    def tribonacci(self, n: int) -> int:
        if n == 0:return 0
        if n < 3:return 1
        
        one_past = self.tri_map[n-1] if self.tri_map[n-1] != -1 else self.tribonacci(n-1)
        two_past = self.tri_map[n-2] if self.tri_map[n-2] != -1 else self.tribonacci(n-2)
        three_past = self.tri_map[n-3] if self.tri_map[n-3] != -1 else self.tribonacci(n-3)

        # T(n) = T(n+3) + T(n-1) + T(n-2)
        self.tri_map[n] = one_past+two_past+three_past

        return self.tri_map[n]