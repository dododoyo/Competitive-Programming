from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if (len(strs) == 1):
            return [[strs[0]]]
    
        anagrams = defaultdict(list)
        
        for i in strs:
            char_freq = [0]*26
            str_freq = ""
            for j in i:
                char_freq[ord(j)-ord('a')] += 1
                
            #can't use list as key value they are mutable
            anagrams[tuple(char_freq)].append(i)
                
            
        return anagrams.values()