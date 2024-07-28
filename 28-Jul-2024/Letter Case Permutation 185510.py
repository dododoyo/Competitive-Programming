# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        solution = []
        n = len(s)
        def backtrack(x, start):

            solution.append("".join(x))
            if start == n:
                return
            for i in range(start, n):
                prev = x[i]
                if 'a' <= x[i] <= 'z':
                    x[i] = x[i].upper()
                elif 'A'<= x[i] <= 'Z':
                    x[i] = x[i].lower()
                else:
                    continue
                backtrack(x, i + 1)
                x[i] = prev

        backtrack(list(s), 0)
        return solution