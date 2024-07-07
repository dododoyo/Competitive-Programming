# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, current_string):
            if len(current_string) == n * 2:
                solution.append(current_string)
                return 

            if left < n:
                backtrack(left + 1, right, current_string + '(')

            if right < left:
                backtrack(left, right + 1, current_string + ')')

        solution = []

        backtrack(0, 0, '')

        return solution