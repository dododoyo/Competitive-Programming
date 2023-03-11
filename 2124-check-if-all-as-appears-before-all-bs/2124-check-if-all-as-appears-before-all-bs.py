class Solution:
    def checkString(self, s: str) -> bool:
        s_len = len(s)
        
        if s_len == 1:
            return 1
        
        prev_char = s[0]
        
        for i in s:
            if i=='a' and prev_char =='b':
                return 0
            prev_char = i
            
        return 1
        