class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        solution = [0]*len(boxes)
        leftCount, rightCount = 0,0
        leftCost,rightCost = 0,0
        for i in range(1, len(boxes)):
            if boxes[i-1] == '1': 
                leftCount += 1
            leftCost += leftCount 
            solution[i] = leftCost
        for i in range(len(boxes)-2, -1, -1):
            if boxes[i+1] == '1': 
                rightCount += 1
            rightCost += rightCount
            solution[i] += rightCost
        return solution