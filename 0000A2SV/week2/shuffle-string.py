class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        solution = [""]*len(s)
        for i in range(len(s)):
            solution[indices[i]] = s[i]
        return "".join(solution)
        