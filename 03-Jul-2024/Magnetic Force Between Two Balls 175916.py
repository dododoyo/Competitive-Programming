# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:

    def maxDistance(self, positions: List[int], m: int) -> int:
        n = len(positions)

        def canPlaceBalls(gap):
            # force equals to gap
            last_position = positions[0]
            balls_remain = m - 1

            for i in range(1,n):
                if positions[i] - last_position >= gap:
                    balls_remain -= 1
                    last_position = positions[i]

                    if balls_remain == 0:
                        return True

            return balls_remain == 0

        positions.sort()

        right = positions[n-1] - positions[0]
        left = 1 
        solution = -1

        while left <= right:
            gap = left + (right-left) // 2

            if canPlaceBalls(gap):
                solution = gap
                left = gap + 1   
            else:
                right = gap - 1   

        return solution