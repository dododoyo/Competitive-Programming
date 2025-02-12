# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def sumDigits(self,num):
        solution = 0
        while num:
            solution += num % 10 
            num = num // 10

        return solution
    def getLucky(self, s: str, k: int) -> int:
        converted = [str(ord(c)-96) for c in s]
        number = int("".join(converted))
        while k:
            number = self.sumDigits(number)
            k -= 1
        return number

        