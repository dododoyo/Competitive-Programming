class Solution:
    def makeGood(self, s: str) -> str:
        s_len = len(s)
        
        #take care of some base cases
        if(s_len == 1):
            return s
        
        stk = [s[0]]
        
        for i in range(1,s_len):
            if(len(stk) == 0):
                stk.append(s[i])
                
            else:
                #easier way to check if not great will be using ascii value
                if(abs(ord(stk[-1]) - ord(s[i])) == 32):
                    stk.pop()
                else:
                    stk.append(s[i])

        return "".join(stk)