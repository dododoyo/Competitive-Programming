class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 == 0:
            solution = num//3
            return [solution-1,solution,solution+1]
        return []
        