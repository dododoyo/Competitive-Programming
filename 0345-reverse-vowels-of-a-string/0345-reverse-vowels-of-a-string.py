class Solution:
    def reverseVowels(self, s: str) -> str:
        #let's use two pointers
        p2 = len(s) - 1
        p1 = 0
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        sol = ""
        
        if(p2 == 0):
            return s
        
        while(p1 < p2):
            if (s[p1] not in vowels and s[p2] not in vowels):
                p1 += 1
                p2 -= 1
            elif (s[p1] in vowels and s[p2] not in vowels): p2 -= 1
            elif (s[p1] not in vowels and s[p2] in vowels): p1 += 1  
            else:
                s = s[:p1] + s[p2] + s[p1+1:p2] + s[p1] + s[p2+1:]
                p1 += 1
                p2 -= 1
        

        return s