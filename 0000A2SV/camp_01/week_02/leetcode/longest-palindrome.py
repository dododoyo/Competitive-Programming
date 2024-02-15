class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_freq,solution,odd_not_seen = defaultdict(int),0,True
        for character in s:
            char_freq[character] += 1
        for value in char_freq.values():
            if value % 2:
                if odd_not_seen:
                    solution += value
                    odd_not_seen = False
                else:
                    solution += value - 1
            else:
                solution += value
        return solution