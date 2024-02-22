class Solution:
    def removeDuplicateLetters(self,s: str) -> str:
        # uses conditional monotonic stack provided that 
        # that character will be occuring again
        stack = []
        
        #use an array to count the occurence of each character
        #since all elements are small letters can use finite sized array
        chr_frq = defaultdict(int)

        for i in s:
            chr_frq[i] += 1
        
        #use a flag array to see if an element is already inserted in the stack
        dont_operate = defaultdict(bool)
        
        """we will generally have two cases either we operate on an element or not
        we want to keep a monotonically increasing stack of characters but not 
        neccesarily if the element will not occur in the future we will keep it 
        even if it ruins the monotonicity"""
        for i in s:
            if(dont_operate[i]):
                chr_frq[i] -= 1
            else:
                while(stack and stack[-1] > i and chr_frq[stack[-1]] != 0):
                    dont_operate[stack[-1]] = False
                    stack.pop()
                
                stack.append(i)
                dont_operate[i] = True
                chr_frq[i] -= 1
            
        return "".join(stack)
