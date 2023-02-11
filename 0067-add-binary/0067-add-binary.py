class Solution:
    def addBinary(self, a: str, b: str) -> str:
        remainder = 0
        res = ""
        
        #adding starts form the last so let's reverse the strings
        a = a[::-1]
        b = b[::-1]
        
        #to make sure we iterate over all of the numbers
        #we use for loop with iteration going to maximimum of both lengths
        
        for i in range(max(len(a),len(b))):
            #take care of the case where a isnot same length as b
            #not to get array index out of bound
            if i >= len(b):
                binaryB = 0
            else:
                binaryB = b[i]
                
            if i >= len(a):
                binaryA = 0
            else:
                binaryA = a[i]
                
            total = int(binaryA) + int(binaryB) + remainder
            
            # 1 + 1 = 0 with remainder 1
            # 1 + 0 = 1 with remainder 1
            # 1 + 1 + 1 = 1 with remainder 1
            
            sumResult = str((total)%2)
            
            res = sumResult + res
            
            remainder = total // 2
            
        if remainder == 1:
            res = "1" + res
            
        return res
        