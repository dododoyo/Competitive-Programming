class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        solution = []
        while i < len(word1) and i < len(word2):
            solution.append(word1[i])
            solution.append(word2[i])
            i+=1
        while i < len(word1):
            solution.append(word1[i])
            i+=1
        while i < len(word2):
            solution.append(word2[i])
            i+=1
        return "".join(solution)
        