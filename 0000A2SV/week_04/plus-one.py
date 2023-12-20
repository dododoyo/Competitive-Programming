class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        for i in range(len(digits)-1,-1,-1):
            result = remainder  + digits[i]
            digits[i],remainder = result%10,result//10 
        if remainder:
            digits = [remainder]+digits
        return digits