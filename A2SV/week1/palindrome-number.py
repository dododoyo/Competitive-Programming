class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        return string_x == string_x[::-1]
    