class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''we can use two pointers pointed at the end
        and at the begining to check if the strings are 
        the same and if they are alphanumerical'''
        #initialize pointers
        p1,p2= 0,len(s) - 1
        #convert every element of string to lowercase
        s = s.lower()
        
        #loop to check if string is valid palindrome
        while(p1 < p2):
            if (not s[p1].isalnum()):p1 += 1;continue
            if (not s[p2].isalnum()):p2 -= 1;continue
            if(s[p1] != s[p2]):return False
            p1 += 1;p2 -= 1
        return True
        