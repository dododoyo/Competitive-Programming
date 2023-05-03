class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        kypr = {'(':')','[':']','{':'}'}
        for i in s:
            if i in kypr.keys():
                stk.append(i)
            elif len(stk) != 0:
                if kypr[stk[-1]] == i:
                    stk.pop()
                else:
                    return False
                
            else:
                return False
        return len(stk) == 0