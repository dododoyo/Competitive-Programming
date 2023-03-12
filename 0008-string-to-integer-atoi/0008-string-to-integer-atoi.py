class Solution:
    def myAtoi(self, s: str) -> int:
        
        s_len = len(s)
        
        negative =  False
        
        solution = 0
        
        start = 0
        #ignore white spaces
        while(start<s_len and s[start] == " "):
            start += 1
        
        #go through each character and use ord() to get the ascii value of each character
        for i in range(start,s_len):
            if(i == start and s[i] == "+"):
                continue
            if(i == start and s[i] == "-"):
                negative = True
                continue  
            if(ord(s[i]) > 47 and ord(s[i]) < 58):
                solution = solution*10 + (ord(s[i]) -48)
            else:
                break
                
        #make sure it is 32 beat integer positive part
        if(not negative and solution > 2147483647):
            return 2147483647
            
        #make sure it is 32 beat integer positive part
        if(negative and (-1*solution) < -2147483648):
            return -2147483648
        
        return (-1*solution) if negative else solution
            