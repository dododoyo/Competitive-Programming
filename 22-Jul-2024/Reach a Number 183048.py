# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:   
        target = abs(target)
        
        def can_reach(i):
            return (i + 1) * i // 2
        
        left, right = 0, target * 2
        while left + 1 < right:            
            middle = (left + right) // 2         
            if can_reach(middle) >= target:
                right = middle
            else:
                left = middle
                
        if can_reach(left) >= target:              
            while can_reach(left) % 2 != target % 2:
                left += 1 
            return left
        if can_reach(right) >= target:
            while can_reach(right) % 2 != target % 2:
                right += 1             
            return right