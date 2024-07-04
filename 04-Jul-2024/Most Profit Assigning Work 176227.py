# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_difficulty = max(difficulty)
        iou = [0] * (max_difficulty + 1)

        for d, p in zip(difficulty, profit):
            iou[d] = max(iou[d], p)

        for i in range(1, max_difficulty + 1):
            iou[i] = max(iou[i], iou[i - 1])

        solution = 0
        for ability in worker:
            if ability > max_difficulty:
                solution += iou[max_difficulty]
            else:
                solution += iou[ability]

        return solution
        