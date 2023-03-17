class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        len_s = len(pattern)
        
        #take care of some base cases
        
        
        s_list = s.split()
        
        if(len_s != len(s_list)):
            return False
        if(len_s == 1):
            return True
            
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