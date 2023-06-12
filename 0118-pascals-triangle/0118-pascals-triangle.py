class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[1]]
        for i in range(numRows-1):
            currentRow = []
            prevRow = [0]+solution[-1]+[0]
            for j in range(len(solution[-1])+1):
                currentRow.append(prevRow[j] + prevRow[j+1])
            solution.append(currentRow)
        return solution;