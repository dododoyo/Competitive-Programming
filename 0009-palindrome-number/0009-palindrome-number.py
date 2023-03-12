class Solution:
    def isPalindrome(self, x: int) -> bool:
        #any negative values are false
        if x < 0:
            return False
        div = 1
        
        #divider is the one used to get the left most number
        #get the divider
        while x >= 10*div:
            div *= 10
        while x:
            # r = x % 10 get the right digit
            # l = x // div get the left digit
            
            if x%10 != x//div:
                return False
            x = (x%div)//10
            div /= 100
        return True