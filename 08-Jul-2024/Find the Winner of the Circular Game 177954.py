# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        solution = 0

        for i in range(1,n+1):
            solution = (solution+k)%i
        
        return solution+1