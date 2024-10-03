# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        solution = 0
        setAllowed = set(allowed)
        for word in words:
            for char in set(word):
                if char not in setAllowed:
                    break
            else:
                solution += 1
        return solution
