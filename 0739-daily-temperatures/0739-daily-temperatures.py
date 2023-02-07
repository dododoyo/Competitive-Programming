#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temper: List[int]) -> List[int]:
        stack = []
        stack.append(len(temper)-1)
        daysHolder = [0]*len(temper)
        daysCounter = 1

        for i in range(len(temper)-2,-1,-1):
            if(temper[stack[-1]] > temper[i]):
                daysHolder[i] = 1
                stack.append(i)
                daysCounter = 1
            else:
                stack.pop()
                daysCounter += 1
                while(len(stack) > 0):
                    if (temper[stack[-1]] > temper[i]):
                        daysHolder[i] = stack[-1] - i
                        stack.append(i)
                        break
                    else:
                        stack.pop()
                        daysCounter += 1
                else:
                    stack.append(i)
                daysCounter = 1

        return daysHolder
        
# @lc code=end

