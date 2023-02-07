#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            #while there are k elements remaining remove
            while stack and k and stack[-1] > i:
                stack.pop()
                k -= 1
            
            if stack or (i is not '0'): #to prevent zeros from being on the start
                stack.append(i)
                
        #if k is not decreased means no element is removed
        #return first k elements of num
        if k:
            stack = stack[0:-k]
            
        return ''.join(stack) or '0'
# @lc code=end

