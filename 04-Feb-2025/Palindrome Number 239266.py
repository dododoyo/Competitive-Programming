# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        result = 0
        while x > 0:
            result *= 10
            result += x % 10
            x //= 10

        return temp == result         

    