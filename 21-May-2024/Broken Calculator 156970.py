# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue > target: 
            return startValue - target
        if startValue == target: 
            return 0

        if target % 2 == 0:
            new_target = target//2
            return 1 + self.brokenCalc(startValue, new_target)
        else:
            return 1 + self.brokenCalc(startValue, target + 1)