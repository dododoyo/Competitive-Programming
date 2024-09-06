# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        bigString = ["Thousand", "Million", "Billion"]
        solution = self.helper(num % 1000)
        num //= 1000
        
        for i in range(3):
            if num > 0 and num % 1000 > 0:
                solution = self.helper(num % 1000) + bigString[i] + " " + solution
            num //= 1000
        
        return solution.strip()

    def helper(self, num: int) -> str:
        ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tenString = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        solution = ""
        if num > 99:
            solution += ones[num // 100] + " Hundred "
        
        num %= 100
        if num < 20 and num > 9:
            solution += tens[num - 10] + " "
        else:
            if num >= 20:
                solution += tenString[num // 10] + " "
            num %= 10
            if num > 0:
                solution += ones[num] + " "
        
        return solution