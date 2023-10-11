class Solution:
    def validPalindrome(self, s: str) -> bool:
        used_chance = False
        l,r = 0,len(s)-1
        while l < r:
            if s[l] == s[r]:
                l,r = l+1,r-1
            else:
                return (self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1]))       
        return True
            
    def isPalindrome(self,s):
        l,r = 0,len(s)-1
        while l < r:
            if s[l] == s[r]:
                l,r = l+1,r-1
            else:
                return False
        return True
        
        