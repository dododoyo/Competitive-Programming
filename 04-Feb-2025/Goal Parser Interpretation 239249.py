# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        solution = []
        n = len(command)

        for i in range(n):
            # check for G 
            if command[i] == "G":
                solution.append("G")

            # check for o 
            if i < n-1:
                if command[i] == "(" and command[i+1] == ")":
                    solution.append("o")

            # check for al
            if i < n-3:
                if command[i:i+4] == "(al)":
                    solution.append("al")

        return "".join(solution)
        