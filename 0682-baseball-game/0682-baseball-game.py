#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i.strip("-").isdigit():
                stack.append(int(i))
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                stack.append(2*stack[-1])
            elif i == "C":
                stack.pop()
            
        return sum(stack)
        
# @lc code=end

