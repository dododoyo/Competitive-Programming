class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      digits = digits[::-1]
      remainder = (digits[0]+1)//10
      result = [(digits[0]+1)%10]
      
      for i in range(1,len(digits)):
        result.append((digits[i]+remainder)%10)
        remainder = (digits[i]+remainder)//10
        
      if remainder:
        result.append(remainder)
      return result[::-1]
        
        