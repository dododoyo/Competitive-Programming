# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        def getBinary(n):
            one = 0
            while n:
                one += n&1
                n = n >> 1
            return one

        solution = []
        for i in range(n+1):
            solution.append(getBinary(i))

        return solution
        