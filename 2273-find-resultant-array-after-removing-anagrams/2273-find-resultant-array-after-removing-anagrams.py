class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        sol = []
        prev = []
        
        for word in words:
            char_freq = [0]*26
            for char in word:
                char_freq[ord(char)-97] += 1
            if prev != char_freq:
                sol.append(word)
                prev = char_freq
        return sol
            
        
            
                
        
        