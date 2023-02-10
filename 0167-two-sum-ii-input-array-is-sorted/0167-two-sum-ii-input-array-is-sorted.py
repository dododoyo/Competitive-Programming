class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstPointer = 0 
        secondPointer = len(numbers) - 1
        
        while(firstPointer < secondPointer):
            if (numbers[firstPointer] + numbers[secondPointer] < target):
                firstPointer += 1
                
            elif (numbers[firstPointer] + numbers[secondPointer] > target):
                secondPointer -= 1
                
            else:
                return [firstPointer+1,secondPointer+1]
            