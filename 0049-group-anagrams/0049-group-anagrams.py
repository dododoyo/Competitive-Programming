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
                str_freq = ""
                for j in range(26):
                    str_freq += chr(j+97) + str(char_freq[j])
                    
            anagrams[str_freq].append(i)
                
        
        solution = []
        
        for i in anagrams:
            solution.append(anagrams[i])
            
        return solution