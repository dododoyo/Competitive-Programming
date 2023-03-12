import math
class Solution:
    def addDigits(self, num: int) -> int: 
        total = 0
        if num < 10:
            return num
        
        while num > 9:  
            
            while num > 0:
                total += (num % 10)
                num //= 10
                
            if(total < 10):
                break
                
            num = total
            total = 0
            
        return total