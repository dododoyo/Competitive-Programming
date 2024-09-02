# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        solution = 0
        n = len(word)
        for i in range(n):
            if word[i] in "aeiou":
                # this char will be part of substrings 0 upto i 
                # and substrings i upto n so it will be counter
                # (i+1)*(n-i) times
                solution += (i+1)*(n-i)

        return solution