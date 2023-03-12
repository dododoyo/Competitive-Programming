class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if(num1 == "0"):
            return num2
        if(num2 == "0"):
            return num1
        
        
        carry = 0
        solution = ""
        len_1 = len(num1)
        
        len_2 = len(num2)
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        #print(num1[::-1])
        if(len_1 > len_2):
            min_ind = len_2
            max_ind = len_1
            max_wrd = 1
        else:
            min_ind = len_1
            max_ind = len_2
            max_wrd = 2
            
            
        i = 0
        
        while(i < min_ind):
            sum_val = int(num1[i]) + int(num2[i]) + carry
            carry = sum_val//10
            solution = solution + str(sum_val%10)
            i += 1
            
        if max_wrd == 1:
            while(i < max_ind):
                sum_val = (int(num1[i]) + carry)
                solution = solution + str(sum_val%10)
                carry = sum_val//10
                i += 1
                
        if max_wrd == 2:
            while(i < max_ind):
                sum_val = (int(num2[i]) + carry)
                solution = solution + str(sum_val%10)
                carry = sum_val//10
                i += 1
                
        if (carry != 0):
            solution = solution + str(carry)
            
        solution = solution[::-1]
        
        return solution
            