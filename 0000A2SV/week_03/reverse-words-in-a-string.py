class Solution:
    def reverseWords(self, s: str) -> str:
        strings = [string for string in s.split() if string != " "]
        return " ".join(strings[::-1])
        