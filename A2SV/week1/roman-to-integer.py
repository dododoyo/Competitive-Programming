class Solution:
    def romanToInt(self, s: str) -> int:
        pointer = 0
        solution = 0
        while pointer < len(s)-1:
            if self.helper(s[pointer]) < self.helper(s[pointer+1]):
                solution += (self.helper(s[pointer+1])-self.helper(s[pointer]))
                pointer += 2
            else:
                solution += self.helper(s[pointer])
                pointer += 1
            print(solution)
        while pointer < len(s):
            solution += self.helper(s[pointer])
            pointer += 1
        return solution

    def helper(self,roman):
        roman_mapper = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        return roman_mapper[roman]
        