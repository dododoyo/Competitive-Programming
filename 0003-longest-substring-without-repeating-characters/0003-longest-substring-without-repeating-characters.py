class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        
        if(len(s) == 0):
            return 0
        
        if(len(s) == 1):
            return 1
        
        r = 1
        l = 0
        max_len = 0
        
        while(r < length):
            if(s[r] in s[l:r]):
                l += 1
            else:
                max_len = max(max_len,r-l+1)
                r += 1
        return max_len
        
        
        