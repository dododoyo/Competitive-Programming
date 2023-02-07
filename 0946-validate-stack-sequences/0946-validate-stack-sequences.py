class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #pushedPointer = 0
        poppedPointer = 0
        
        # use stack to check values
        stack = []
        
        for i in pushed:
            stack.append(i)
            while(len(stack)>0 and stack[-1] == popped[poppedPointer]):
                stack.pop()
                poppedPointer += 1
        
        return len(stack)==0
            