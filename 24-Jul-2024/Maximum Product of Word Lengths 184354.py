# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        letters = [0] * n

        for i in range(n):
            for character in words[i]:
                letters[i] |= 1 << (ord(character)-97)

        solution = 0

        for i in range(n):
            for j in range(i+1, n):
                if not (letters[i] & letters[j]):
                    solution = max(solution, len(words[i])*len(words[j]))
        return solution