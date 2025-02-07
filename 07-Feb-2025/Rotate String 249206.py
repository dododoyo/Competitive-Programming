# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # edge cases 
        if len(s) != len(goal):
            return False

        long_s = s + s 

        return goal in long_s