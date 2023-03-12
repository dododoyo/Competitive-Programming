class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1_len = len(num1)
        n2_len = len(num2)
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        solution = [0]*(n1_len + n2_len)
        
        carry = 0
        for i in range(n1_len):
            for j in range(n2_len):
                num = int(num1[i])*int(num2[j])
                
                real_num = solution[i+j] + num
                
                
                solution[i+j] = real_num%10
                
                solution[i+j+1] += real_num//10
                
        
        
        begin = 0
        #reverse the solution
        solution = solution[::-1]
        
        #remove leading zeros
        while (begin < (n1_len+n2_len)) and solution[begin] == 0:
            begin += 1
            
        #convert array to string from beginning
        solution = map(str, solution[begin:])
        
        return "".join(solution)