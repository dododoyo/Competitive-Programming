class Solution:
    def makeGood(self, s: str) -> str:
        s_len = len(s)
        
        #take care of some base cases
        if(s_len == 1):
            return s
        
        stk = []
        
        for i in s:
            if(len(stk) == 0):
                stk.append(i)
                
            else:
                #easier way to check if not great will be using ascii value
                if(abs(ord(stk[-1]) - ord(i)) == 32):
                    stk.pop()
                else:
                    stk.append(i)

        return "".join(stk)