class Solution:
    def reverseWords(self, s: str) -> str:
        each_word = s.split()
        
        solution = each_word[0]
        
        length = len(each_word)
        
        for i in range(1,length):
            solution = each_word[i] + " " + solution
            
        return solution
        