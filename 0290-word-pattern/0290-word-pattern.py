class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        len_s = len(pattern)
        
        
        s_list = s.split()
        
        #take care of some base cases
        
        #if the length of the pattern and the string aren't
        #same return false
        if(len_s != len(s_list)):
            return False
        
        #if the length is the same and length of s is 1
        #return true
        if(len_s == 1):
            return True
        #dealing with base cases over!
        
        
        s_dict = {}
        
        for i in range(len_s):
            
            if pattern[i] in s_dict and s_list[i] != s_dict[pattern[i]]:
                return False
                
            elif pattern[i] in s_dict and s_list[i] == s_dict[pattern[i]]:
                continue
                
            elif pattern[i] not in s_dict and s_list[i] in s_dict.values():
                return False
            
            s_dict[pattern[i]] = s_list[i]
        
        return True            
    
    #space O(m) where m = number of distinct characters in pattern
    #time O(n)  where n = length of pattern string'