class Solution:
    def removeStars(self, s: str) -> str:
        solution = []
        for char in s:
            if char == "*" and solution:
                solution.pop()
            else:
                solution.append(char)
        return "".join(solution)
