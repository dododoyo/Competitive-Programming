class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        
        for i in s:
            if(len(stk) == 0):
                stk.append(i)
                
            else:
                # if the last element checked and the element after it are
                # not good remove the one in the stack and don't append 
                # the one that is checked now
                if(abs(ord(stk[-1]) - ord(i)) == 32):
                # easier way to check if not great will be using ascii value
                    stk.pop()
                
                # if they are good it can be added to the string
                else:
                    stk.append(i)

        return "".join(stk)
    
        #time O(n)
        #space O(n)