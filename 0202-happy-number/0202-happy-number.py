class Solution:
    def isHappy(self, n: int) -> bool:
        tracked_numbers = set()
        
        while True:
            total = 0
            i = 0
            while n != 0:
                
                total += pow(n%10,2)
                n //= 10
                
            if total == 1:
                return True
            
            n = total
            
            if total in tracked_numbers:
                return False
            else:
                tracked_numbers.add(total)
            
        