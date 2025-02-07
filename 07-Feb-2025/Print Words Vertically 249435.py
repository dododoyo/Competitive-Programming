# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        longest = 0
        splitted = s.split()

        for word in splitted:
            longest = max(longest,len(word))

        solution = []
        for i in range(longest):
            curr = []

            for j in range(len(splitted)):

                if i >= len(splitted[j]):
                    curr.append(" ")
                else:
                    curr.append(splitted[j][i])
            
            while curr[-1] == " ":
                curr.pop()
                
            solution.append("".join(curr))
        
        return solution
